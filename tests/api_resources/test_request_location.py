# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import RequestLocationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequestLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: SendblueAPI) -> None:
        request_location = client.request_location.create(
            from_number="+18887776666",
            number="+19998887777",
        )
        assert_matches_type(RequestLocationCreateResponse, request_location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SendblueAPI) -> None:
        response = client.request_location.with_raw_response.create(
            from_number="+18887776666",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_location = response.parse()
        assert_matches_type(RequestLocationCreateResponse, request_location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SendblueAPI) -> None:
        with client.request_location.with_streaming_response.create(
            from_number="+18887776666",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_location = response.parse()
            assert_matches_type(RequestLocationCreateResponse, request_location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRequestLocation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSendblueAPI) -> None:
        request_location = await async_client.request_location.create(
            from_number="+18887776666",
            number="+19998887777",
        )
        assert_matches_type(RequestLocationCreateResponse, request_location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.request_location.with_raw_response.create(
            from_number="+18887776666",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_location = await response.parse()
        assert_matches_type(RequestLocationCreateResponse, request_location, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.request_location.with_streaming_response.create(
            from_number="+18887776666",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_location = await response.parse()
            assert_matches_type(RequestLocationCreateResponse, request_location, path=["response"])

        assert cast(Any, response.is_closed) is True
