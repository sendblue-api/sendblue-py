# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types.v2 import TotpGetCodeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTotp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_code(self, client: SendblueAPI) -> None:
        totp = client.v2.totp.get_code(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(TotpGetCodeResponse, totp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_code(self, client: SendblueAPI) -> None:
        response = client.v2.totp.with_raw_response.get_code(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        totp = response.parse()
        assert_matches_type(TotpGetCodeResponse, totp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_code(self, client: SendblueAPI) -> None:
        with client.v2.totp.with_streaming_response.get_code(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            totp = response.parse()
            assert_matches_type(TotpGetCodeResponse, totp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_code(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.v2.totp.with_raw_response.get_code(
                "",
            )


class TestAsyncTotp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_code(self, async_client: AsyncSendblueAPI) -> None:
        totp = await async_client.v2.totp.get_code(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(TotpGetCodeResponse, totp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_code(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.totp.with_raw_response.get_code(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        totp = await response.parse()
        assert_matches_type(TotpGetCodeResponse, totp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_code(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.totp.with_streaming_response.get_code(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            totp = await response.parse()
            assert_matches_type(TotpGetCodeResponse, totp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_code(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.v2.totp.with_raw_response.get_code(
                "",
            )
