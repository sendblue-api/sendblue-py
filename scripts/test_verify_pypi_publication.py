"""Run offline with: python3 -m unittest scripts.test_verify_pypi_publication."""

from __future__ import annotations

import io
import sys
import json
import hashlib
import tempfile
import unittest
from typing import TYPE_CHECKING, Any
from pathlib import Path
from contextlib import ExitStack, redirect_stderr, redirect_stdout
from urllib.error import URLError, HTTPError
from email.message import Message
from unittest.mock import Mock, patch

if TYPE_CHECKING or sys.version_info < (3, 12):
    from typing_extensions import override
else:
    from typing import override

from scripts import verify_pypi_publication as publication

ARTIFACTS = {"sendblue-1.0.0-py3-none-any.whl": "a" * 64, "sendblue-1.0.0.tar.gz": "b" * 64}


def metadata(artifacts: dict[str, str]) -> dict[str, object]:
    return {"urls": [{"filename": name, "digests": {"sha256": digest}} for name, digest in artifacts.items()]}


class ArtifactTests(unittest.TestCase):
    def test_absent_release_needs_all_artifacts(self) -> None:
        self.assertEqual(publication.missing_artifacts(ARTIFACTS, None), sorted(ARTIFACTS))

    def test_matching_release_needs_no_artifacts(self) -> None:
        self.assertEqual(publication.missing_artifacts(ARTIFACTS, metadata(ARTIFACTS)), [])

    def test_partial_release_needs_only_missing_artifact(self) -> None:
        wheel = next(iter(ARTIFACTS))
        self.assertEqual(
            publication.missing_artifacts(ARTIFACTS, metadata({wheel: ARTIFACTS[wheel]})),
            ["sendblue-1.0.0.tar.gz"],
        )

    def test_conflicting_digest_cannot_be_skipped(self) -> None:
        wheel = next(iter(ARTIFACTS))
        with self.assertRaisesRegex(RuntimeError, "differs from local build"):
            publication.missing_artifacts(ARTIFACTS, metadata({wheel: "c" * 64}))

    def test_yanked_matching_file_is_not_success(self) -> None:
        wheel = next(iter(ARTIFACTS))
        remote = {"urls": [{"filename": wheel, "digests": {"sha256": ARTIFACTS[wheel]}, "yanked": True}]}
        with self.assertRaisesRegex(RuntimeError, "yanked"):
            publication.missing_artifacts(ARTIFACTS, remote)

    def test_malformed_metadata_is_not_an_absent_release(self) -> None:
        entry = {"filename": "sendblue-1.0.0.tar.gz", "digests": {"sha256": "b" * 64}}
        invalid: list[dict[str, Any]] = [
            {},
            {"urls": None},
            {"urls": {}},
            {"urls": [None]},
            {"urls": [{"filename": "missing-digest"}]},
            {"urls": [{"filename": "bad-digest", "digests": {"sha256": "invalid"}}]},
            {"urls": [entry, entry]},
        ]
        for remote in invalid:
            with self.subTest(remote=remote), self.assertRaises(publication.RegistryError):
                publication.missing_artifacts(ARTIFACTS, remote)

    def test_hashes_all_built_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for filename in ARTIFACTS:
                (root / filename).write_bytes(filename.encode())
            expected = {filename: hashlib.sha256(filename.encode()).hexdigest() for filename in ARTIFACTS}
            self.assertEqual(publication.local_artifacts(root), expected)

    def test_requires_wheel_and_source_distribution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(RuntimeError):
                publication.local_artifacts(root)
            (root / "sendblue-1.0.0.tar.gz").write_bytes(b"source")
            with self.assertRaisesRegex(RuntimeError, "Both wheel and source"):
                publication.local_artifacts(root)


class RegistryTests(unittest.TestCase):
    def test_only_404_means_absent(self) -> None:
        for status in (401, 403, 404, 429, 500, 503):
            error = HTTPError("https://pypi.org/", status, "test error", Message(), None)
            with self.subTest(status=status), patch.object(publication, "urlopen", side_effect=error):
                if status == 404:
                    self.assertIsNone(publication.fetch_release("sendblue", "1.0.0"))
                else:
                    with self.assertRaises(publication.RegistryError) as raised:
                        publication.fetch_release("sendblue", "1.0.0")
                    self.assertEqual(raised.exception.retryable, status == 429 or status >= 500)

    def test_transport_failure_is_retryable_not_absent(self) -> None:
        with patch.object(publication, "urlopen", side_effect=URLError("unavailable")):
            with self.assertRaises(publication.RegistryError) as raised:
                publication.fetch_release("sendblue", "1.0.0")
            self.assertTrue(raised.exception.retryable)

    def test_exact_version_endpoint(self) -> None:
        with patch.object(
            publication, "urlopen", return_value=io.BytesIO(json.dumps(metadata(ARTIFACTS)).encode())
        ) as get:
            self.assertEqual(publication.fetch_release("sendblue", "1.0.0"), metadata(ARTIFACTS))
        self.assertEqual(get.call_args.args[0].full_url, "https://pypi.org/pypi/sendblue/1.0.0/json")

    def test_invalid_json_and_nonobject_response_fail(self) -> None:
        for body in (b"not-json", b"[]", b"null"):
            with self.subTest(body=body), patch.object(publication, "urlopen", return_value=io.BytesIO(body)):
                with self.assertRaises(publication.RegistryError) as raised:
                    publication.fetch_release("sendblue", "1.0.0")
                self.assertFalse(raised.exception.retryable)

    def test_visibility_retry_recovers_transient_error_and_absence(self) -> None:
        responses = [publication.RegistryError("unavailable", retryable=True), None, metadata(ARTIFACTS)]
        with patch.object(publication, "fetch_release", side_effect=responses), patch.object(
            publication.time, "sleep"
        ) as sleep, redirect_stderr(io.StringIO()):
            publication.verify_publication("sendblue", "1.0.0", ARTIFACTS, attempts=3)
        self.assertEqual(sleep.call_count, 2)

    def test_visibility_failure_is_bounded(self) -> None:
        with patch.object(publication, "fetch_release", return_value=None) as fetch, patch.object(
            publication.time, "sleep"
        ) as sleep, redirect_stderr(io.StringIO()):
            with self.assertRaisesRegex(RuntimeError, "Publication was not verified"):
                publication.verify_publication("sendblue", "1.0.0", ARTIFACTS, attempts=2)
        self.assertEqual(fetch.call_count, 2)
        sleep.assert_called_once()

    def test_auth_error_stops_without_visibility_retry(self) -> None:
        with patch.object(publication, "fetch_release", side_effect=publication.RegistryError("HTTP 403")) as fetch:
            with self.assertRaisesRegex(publication.RegistryError, "HTTP 403"):
                publication.verify_publication("sendblue", "1.0.0", ARTIFACTS, attempts=3)
        fetch.assert_called_once()


class PublicationTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        stack = ExitStack()
        self.addCleanup(stack.close)
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "pyproject.toml").write_text('[project]\nname = "sendblue"\nversion = "1.0.0"\n')
        stack.enter_context(patch.object(publication, "__file__", str(self.root / "scripts" / "verify.py")))
        stack.enter_context(patch.object(publication, "local_artifacts", return_value=ARTIFACTS))
        stack.enter_context(patch.dict(publication.os.environ, {"PYPI_TOKEN": "test-token"}))
        self.publish_run: Mock = stack.enter_context(
            patch.object(publication.subprocess, "run", return_value=Mock(returncode=0))
        )
        self.sleep: Mock = stack.enter_context(patch.object(publication.time, "sleep"))
        stack.enter_context(redirect_stderr(io.StringIO()))
        stack.enter_context(redirect_stdout(io.StringIO()))

    def test_complete_release_skips_upload_without_credentials(self) -> None:
        with patch.object(publication, "fetch_release", return_value=metadata(ARTIFACTS)), patch.dict(
            publication.os.environ, {}, clear=True
        ):
            self.assertEqual(publication.main(), 0)
        self.publish_run.assert_not_called()

    def test_partial_release_uploads_only_missing_distribution(self) -> None:
        wheel = next(iter(ARTIFACTS))
        with patch.object(
            publication, "fetch_release", side_effect=[metadata({wheel: ARTIFACTS[wheel]}), metadata(ARTIFACTS)]
        ):
            self.assertEqual(publication.main(), 0)
        self.publish_run.assert_called_once_with(
            ["rye", "publish", "--yes", "--token", "test-token", str(self.root / "dist" / "sendblue-1.0.0.tar.gz")],
            cwd=self.root,
            check=False,
        )

    def test_uncertain_upload_success_is_verified_without_second_upload(self) -> None:
        self.publish_run.return_value.returncode = 1
        with patch.object(publication, "fetch_release", side_effect=[None, None, metadata(ARTIFACTS)]):
            self.assertEqual(publication.main(), 0)
        self.publish_run.assert_called_once()
        self.sleep.assert_called_once()

    def test_upload_failure_stays_failed_if_registry_never_confirms(self) -> None:
        self.publish_run.return_value.returncode = 1
        with patch.object(publication, "fetch_release", return_value=None):
            with self.assertRaisesRegex(RuntimeError, "Publication was not verified"):
                publication.main()
        self.publish_run.assert_called_once()

    def test_conflicting_release_never_uploads(self) -> None:
        wheel = next(iter(ARTIFACTS))
        with patch.object(publication, "fetch_release", return_value=metadata({wheel: "c" * 64})):
            with self.assertRaisesRegex(RuntimeError, "differs from local build"):
                publication.main()
        self.publish_run.assert_not_called()

    def test_preflight_registry_failure_never_uploads(self) -> None:
        with patch.object(publication, "fetch_release", side_effect=publication.RegistryError("HTTP 503")):
            with self.assertRaises(publication.RegistryError):
                publication.main()
        self.publish_run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
