# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types.v2 import (
    SeatListResponse,
    SeatCountResponse,
    SeatRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        seat = client.v2.seats.retrieve(
            "seat_id",
        )
        assert_matches_type(SeatRetrieveResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.v2.seats.with_raw_response.retrieve(
            "seat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = response.parse()
        assert_matches_type(SeatRetrieveResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.v2.seats.with_streaming_response.retrieve(
            "seat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = response.parse()
            assert_matches_type(SeatRetrieveResponse, seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `seat_id` but received ''"):
            client.v2.seats.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: SendblueAPI) -> None:
        seat = client.v2.seats.list()
        assert_matches_type(SeatListResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: SendblueAPI) -> None:
        seat = client.v2.seats.list(
            email="dev@stainless.com",
            limit=0,
            offset=0,
        )
        assert_matches_type(SeatListResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SendblueAPI) -> None:
        response = client.v2.seats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = response.parse()
        assert_matches_type(SeatListResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SendblueAPI) -> None:
        with client.v2.seats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = response.parse()
            assert_matches_type(SeatListResponse, seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_count(self, client: SendblueAPI) -> None:
        seat = client.v2.seats.count()
        assert_matches_type(SeatCountResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_count_with_all_params(self, client: SendblueAPI) -> None:
        seat = client.v2.seats.count(
            email="dev@stainless.com",
        )
        assert_matches_type(SeatCountResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: SendblueAPI) -> None:
        response = client.v2.seats.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = response.parse()
        assert_matches_type(SeatCountResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: SendblueAPI) -> None:
        with client.v2.seats.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = response.parse()
            assert_matches_type(SeatCountResponse, seat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSeats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        seat = await async_client.v2.seats.retrieve(
            "seat_id",
        )
        assert_matches_type(SeatRetrieveResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.seats.with_raw_response.retrieve(
            "seat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = await response.parse()
        assert_matches_type(SeatRetrieveResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.seats.with_streaming_response.retrieve(
            "seat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = await response.parse()
            assert_matches_type(SeatRetrieveResponse, seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `seat_id` but received ''"):
            await async_client.v2.seats.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSendblueAPI) -> None:
        seat = await async_client.v2.seats.list()
        assert_matches_type(SeatListResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        seat = await async_client.v2.seats.list(
            email="dev@stainless.com",
            limit=0,
            offset=0,
        )
        assert_matches_type(SeatListResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.seats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = await response.parse()
        assert_matches_type(SeatListResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.seats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = await response.parse()
            assert_matches_type(SeatListResponse, seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncSendblueAPI) -> None:
        seat = await async_client.v2.seats.count()
        assert_matches_type(SeatCountResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        seat = await async_client.v2.seats.count(
            email="dev@stainless.com",
        )
        assert_matches_type(SeatCountResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.seats.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = await response.parse()
        assert_matches_type(SeatCountResponse, seat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.seats.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = await response.parse()
            assert_matches_type(SeatCountResponse, seat, path=["response"])

        assert cast(Any, response.is_closed) is True
