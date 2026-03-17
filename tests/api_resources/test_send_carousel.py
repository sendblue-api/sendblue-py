# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import SendCarouselSendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSendCarousel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: SendblueAPI) -> None:
        send_carousel = client.send_carousel.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
        )
        assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: SendblueAPI) -> None:
        send_carousel = client.send_carousel.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
            metadata={},
            send_style="celebration",
            status_callback="https://example.com/webhook",
        )
        assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: SendblueAPI) -> None:
        response = client.send_carousel.with_raw_response.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send_carousel = response.parse()
        assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: SendblueAPI) -> None:
        with client.send_carousel.with_streaming_response.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send_carousel = response.parse()
            assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSendCarousel:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncSendblueAPI) -> None:
        send_carousel = await async_client.send_carousel.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
        )
        assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        send_carousel = await async_client.send_carousel.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
            metadata={},
            send_style="celebration",
            status_callback="https://example.com/webhook",
        )
        assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.send_carousel.with_raw_response.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send_carousel = await response.parse()
        assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.send_carousel.with_streaming_response.send(
            from_number="+19998887777",
            media_urls=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
                "https://example.com/image3.jpg",
            ],
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send_carousel = await response.parse()
            assert_matches_type(SendCarouselSendResponse, send_carousel, path=["response"])

        assert cast(Any, response.is_closed) is True
