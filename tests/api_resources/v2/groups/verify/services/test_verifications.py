# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types.v2.groups.verify.services import (
    VerificationCreateResponse,
    VerificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: SendblueAPI) -> None:
        verification = client.v2.groups.verify.services.verifications.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: SendblueAPI) -> None:
        verification = client.v2.groups.verify.services.verifications.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
            hosted={
                "parent_origin": "https://app.example.com",
                "accent_color": "#008BFF",
                "brand_name": "Acme",
                "theme": "light",
            },
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SendblueAPI) -> None:
        response = client.v2.groups.verify.services.verifications.with_raw_response.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SendblueAPI) -> None:
        with client.v2.groups.verify.services.verifications.with_streaming_response.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_sid` but received ''"):
            client.v2.groups.verify.services.verifications.with_raw_response.create(
                service_sid="",
                to="+14155551212",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        verification = client.v2.groups.verify.services.verifications.retrieve(
            verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.v2.groups.verify.services.verifications.with_raw_response.retrieve(
            verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.v2.groups.verify.services.verifications.with_streaming_response.retrieve(
            verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_sid` but received ''"):
            client.v2.groups.verify.services.verifications.with_raw_response.retrieve(
                verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                service_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_sid` but received ''"):
            client.v2.groups.verify.services.verifications.with_raw_response.retrieve(
                verification_sid="",
                service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )


class TestAsyncVerifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSendblueAPI) -> None:
        verification = await async_client.v2.groups.verify.services.verifications.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        verification = await async_client.v2.groups.verify.services.verifications.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
            hosted={
                "parent_origin": "https://app.example.com",
                "accent_color": "#008BFF",
                "brand_name": "Acme",
                "theme": "light",
            },
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.groups.verify.services.verifications.with_raw_response.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.groups.verify.services.verifications.with_streaming_response.create(
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            to="+14155551212",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_sid` but received ''"):
            await async_client.v2.groups.verify.services.verifications.with_raw_response.create(
                service_sid="",
                to="+14155551212",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        verification = await async_client.v2.groups.verify.services.verifications.retrieve(
            verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.groups.verify.services.verifications.with_raw_response.retrieve(
            verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.groups.verify.services.verifications.with_streaming_response.retrieve(
            verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_sid` but received ''"):
            await async_client.v2.groups.verify.services.verifications.with_raw_response.retrieve(
                verification_sid="VRE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
                service_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_sid` but received ''"):
            await async_client.v2.groups.verify.services.verifications.with_raw_response.retrieve(
                verification_sid="",
                service_sid="SVE1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
            )
