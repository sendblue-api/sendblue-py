# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sendblue_api import SendblueAPI, AsyncSendblueAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: SendblueAPI) -> None:
        event_stream = client.events.stream()
        event_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: SendblueAPI) -> None:
        event_stream = client.events.stream(
            types="message.received,message.updated,typing.changed",
        )
        event_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: SendblueAPI) -> None:
        response = client.events.with_raw_response.stream()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: SendblueAPI) -> None:
        with client.events.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncSendblueAPI) -> None:
        event_stream = await async_client.events.stream()
        await event_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        event_stream = await async_client.events.stream(
            types="message.received,message.updated,typing.changed",
        )
        await event_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.events.with_raw_response.stream()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.events.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
