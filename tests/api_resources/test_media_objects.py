# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import MediaObjectUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMediaObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: SendblueAPI) -> None:
        media_object = client.media_objects.upload(
            media_url="https://example.com/image.jpg",
        )
        assert_matches_type(MediaObjectUploadResponse, media_object, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: SendblueAPI) -> None:
        response = client.media_objects.with_raw_response.upload(
            media_url="https://example.com/image.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_object = response.parse()
        assert_matches_type(MediaObjectUploadResponse, media_object, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: SendblueAPI) -> None:
        with client.media_objects.with_streaming_response.upload(
            media_url="https://example.com/image.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_object = response.parse()
            assert_matches_type(MediaObjectUploadResponse, media_object, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMediaObjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncSendblueAPI) -> None:
        media_object = await async_client.media_objects.upload(
            media_url="https://example.com/image.jpg",
        )
        assert_matches_type(MediaObjectUploadResponse, media_object, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.media_objects.with_raw_response.upload(
            media_url="https://example.com/image.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_object = await response.parse()
        assert_matches_type(MediaObjectUploadResponse, media_object, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.media_objects.with_streaming_response.upload(
            media_url="https://example.com/image.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_object = await response.parse()
            assert_matches_type(MediaObjectUploadResponse, media_object, path=["response"])

        assert cast(Any, response.is_closed) is True
