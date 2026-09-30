#!/usr/bin/env python3
"""Publish missing artifacts once and verify the exact release on public PyPI.

Requires Python 3.11+ independently of the library's supported Python versions.
"""

from __future__ import annotations

import os
import re
import sys
import json
import time
import hashlib
import subprocess
from typing import Any, cast
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

import tomllib


class RegistryError(RuntimeError):
    def __init__(self, message: str, *, retryable: bool = False) -> None:
        super().__init__(message)
        self.retryable = retryable


def local_artifacts(directory: Path) -> dict[str, str]:
    """Return filenames and SHA256 digests for every built distribution."""
    paths = sorted(directory.iterdir())
    if not paths or any(not p.is_file() or not p.name.endswith((".whl", ".tar.gz")) for p in paths):
        raise RuntimeError("dist must contain only built wheels and source distributions")
    if not any(p.name.endswith(".whl") for p in paths) or not any(p.name.endswith(".tar.gz") for p in paths):
        raise RuntimeError("Both wheel and source distribution are required")
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def missing_artifacts(local: dict[str, str], metadata: dict[str, Any] | None) -> list[str]:
    """Fail on immutable filename conflicts; return only files safe to upload."""
    if metadata is None:
        return sorted(local)
    try:
        entries = metadata["urls"]
        if not isinstance(entries, list):
            raise ValueError("urls must be a list")
        remote: dict[str, str] = {}
        for entry in cast(list[Any], entries):
            filename = entry["filename"]
            digest = entry["digests"]["sha256"]
            if (
                not isinstance(filename, str)
                or not isinstance(digest, str)
                or not re.fullmatch(r"[0-9a-f]{64}", digest)
            ):
                raise ValueError("invalid filename or SHA256 digest")
            if filename in remote:
                raise ValueError("duplicate filename")
            remote[filename] = digest
            if filename in local and entry.get("yanked"):
                raise RuntimeError(f"Published artifact is yanked: {filename}")
    except (KeyError, TypeError, ValueError) as exc:
        raise RegistryError("PyPI returned malformed artifact metadata") from exc
    for filename, digest in local.items():
        if filename in remote and remote[filename] != digest:
            raise RuntimeError(f"Published artifact differs from local build: {filename}")
    return sorted(set(local) - remote.keys())


def fetch_release(project: str, version: str) -> dict[str, Any] | None:
    # Exact-version endpoint documented at https://docs.pypi.org/api/json/.
    url = f"https://pypi.org/pypi/{quote(project, safe='')}/{quote(version, safe='')}/json"
    request = Request(url, headers={"Accept": "application/json", "Cache-Control": "no-cache"})
    try:
        with urlopen(request, timeout=20) as response:
            metadata = json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise RegistryError(
            f"PyPI metadata request failed: HTTP {exc.code}", retryable=exc.code == 429 or exc.code >= 500
        ) from exc
    except (URLError, TimeoutError) as exc:
        raise RegistryError(f"PyPI metadata request failed: {exc}", retryable=True) from exc
    except (ValueError, UnicodeError) as exc:
        raise RegistryError("PyPI returned invalid JSON metadata") from exc
    if not isinstance(metadata, dict):
        raise RegistryError("PyPI returned invalid release metadata")
    return cast(dict[str, Any], metadata)


def verify_publication(
    project: str, version: str, artifacts: dict[str, str], *, attempts: int = 12, delay: int = 10
) -> None:
    """Wait a bounded period for visibility, never submit another upload."""
    if attempts < 1:
        raise ValueError("attempts must be positive")
    last_error = "Release is not visible"
    for attempt in range(attempts):
        try:
            missing = missing_artifacts(artifacts, fetch_release(project, version))
            if not missing:
                return
            last_error = f"PyPI is missing artifacts: {', '.join(missing)}"
        except RegistryError as exc:
            if not exc.retryable:
                raise
            last_error = str(exc)
        print(f"Verification {attempt + 1}/{attempts}: {last_error}", file=sys.stderr)
        if attempt + 1 < attempts:
            time.sleep(delay)
    raise RuntimeError(f"Publication was not verified: {last_error}")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    with (root / "pyproject.toml").open("rb") as stream:
        project = tomllib.load(stream)["project"]
    name, version = project["name"], project["version"]
    artifacts = local_artifacts(root / "dist")
    missing = missing_artifacts(artifacts, fetch_release(name, version))
    if not missing:
        print(f"Verified {name} {version}: all artifacts are already published")
        return 0
    token = os.environ.get("PYPI_TOKEN")
    if not token:
        raise RuntimeError("PYPI_TOKEN is required to upload missing artifacts")
    # Rye accepts explicit distribution paths: https://rye.astral.sh/guide/commands/publish/.
    # Do not use check=True: its exception would include the token-bearing command.
    result = subprocess.run(
        ["rye", "publish", "--yes", "--token", token, *[str(root / "dist" / filename) for filename in missing]],
        cwd=root,
        check=False,
    )
    if result.returncode:
        print(f"Rye publish exited {result.returncode}; checking whether the upload completed", file=sys.stderr)
    verify_publication(name, version, artifacts)
    print(f"Verified {name} {version}: every local artifact matches public PyPI")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"Publication failed: {error}", file=sys.stderr)
        sys.exit(1)
