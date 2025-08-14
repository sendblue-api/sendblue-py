# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types.contacts import BulkCreateResponse, BulkDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: SendblueAPI) -> None:
        bulk = client.contacts.bulk.create(
            contacts=[{"phone": "phone"}],
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SendblueAPI) -> None:
        response = client.contacts.bulk.with_raw_response.create(
            contacts=[{"phone": "phone"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SendblueAPI) -> None:
        with client.contacts.bulk.with_streaming_response.create(
            contacts=[{"phone": "phone"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: SendblueAPI) -> None:
        bulk = client.contacts.bulk.delete(
            contact_ids=["+1234567890", "+0987654321"],
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SendblueAPI) -> None:
        response = client.contacts.bulk.with_raw_response.delete(
            contact_ids=["+1234567890", "+0987654321"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SendblueAPI) -> None:
        with client.contacts.bulk.with_streaming_response.delete(
            contact_ids=["+1234567890", "+0987654321"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSendblueAPI) -> None:
        bulk = await async_client.contacts.bulk.create(
            contacts=[{"phone": "phone"}],
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.bulk.with_raw_response.create(
            contacts=[{"phone": "phone"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.bulk.with_streaming_response.create(
            contacts=[{"phone": "phone"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSendblueAPI) -> None:
        bulk = await async_client.contacts.bulk.delete(
            contact_ids=["+1234567890", "+0987654321"],
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.bulk.with_raw_response.delete(
            contact_ids=["+1234567890", "+0987654321"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.bulk.with_streaming_response.delete(
            contact_ids=["+1234567890", "+0987654321"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
