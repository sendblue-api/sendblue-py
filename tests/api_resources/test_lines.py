# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import LineGetStateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_state(self, client: SendblueAPI) -> None:
        line = client.lines.get_state()
        assert_matches_type(LineGetStateResponse, line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_state(self, client: SendblueAPI) -> None:
        response = client.lines.with_raw_response.get_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line = response.parse()
        assert_matches_type(LineGetStateResponse, line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_state(self, client: SendblueAPI) -> None:
        with client.lines.with_streaming_response.get_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line = response.parse()
            assert_matches_type(LineGetStateResponse, line, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_state(self, async_client: AsyncSendblueAPI) -> None:
        line = await async_client.lines.get_state()
        assert_matches_type(LineGetStateResponse, line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_state(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.lines.with_raw_response.get_state()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        line = await response.parse()
        assert_matches_type(LineGetStateResponse, line, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_state(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.lines.with_streaming_response.get_state() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            line = await response.parse()
            assert_matches_type(LineGetStateResponse, line, path=["response"])

        assert cast(Any, response.is_closed) is True
