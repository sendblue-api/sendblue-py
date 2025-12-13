# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import TypingIndicatorSendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTypingIndicators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: SendblueAPI) -> None:
        typing_indicator = client.typing_indicators.send(
            from_number="+16292925296",
            number="+19998887777",
        )
        assert_matches_type(TypingIndicatorSendResponse, typing_indicator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: SendblueAPI) -> None:
        response = client.typing_indicators.with_raw_response.send(
            from_number="+16292925296",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typing_indicator = response.parse()
        assert_matches_type(TypingIndicatorSendResponse, typing_indicator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: SendblueAPI) -> None:
        with client.typing_indicators.with_streaming_response.send(
            from_number="+16292925296",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            typing_indicator = response.parse()
            assert_matches_type(TypingIndicatorSendResponse, typing_indicator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTypingIndicators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncSendblueAPI) -> None:
        typing_indicator = await async_client.typing_indicators.send(
            from_number="+16292925296",
            number="+19998887777",
        )
        assert_matches_type(TypingIndicatorSendResponse, typing_indicator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.typing_indicators.with_raw_response.send(
            from_number="+16292925296",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        typing_indicator = await response.parse()
        assert_matches_type(TypingIndicatorSendResponse, typing_indicator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.typing_indicators.with_streaming_response.send(
            from_number="+16292925296",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            typing_indicator = await response.parse()
            assert_matches_type(TypingIndicatorSendResponse, typing_indicator, path=["response"])

        assert cast(Any, response.is_closed) is True
