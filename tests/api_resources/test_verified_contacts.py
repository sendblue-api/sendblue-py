# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import (
    VerifiedContactListResponse,
    VerifiedContactCreateResponse,
    VerifiedContactRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifiedContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: SendblueAPI) -> None:
        verified_contact = client.verified_contacts.create(
            phone_number="+12125550199",
        )
        assert_matches_type(VerifiedContactCreateResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SendblueAPI) -> None:
        response = client.verified_contacts.with_raw_response.create(
            phone_number="+12125550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_contact = response.parse()
        assert_matches_type(VerifiedContactCreateResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SendblueAPI) -> None:
        with client.verified_contacts.with_streaming_response.create(
            phone_number="+12125550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_contact = response.parse()
            assert_matches_type(VerifiedContactCreateResponse, verified_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        verified_contact = client.verified_contacts.retrieve(
            "+12125550199",
        )
        assert_matches_type(VerifiedContactRetrieveResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.verified_contacts.with_raw_response.retrieve(
            "+12125550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_contact = response.parse()
        assert_matches_type(VerifiedContactRetrieveResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.verified_contacts.with_streaming_response.retrieve(
            "+12125550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_contact = response.parse()
            assert_matches_type(VerifiedContactRetrieveResponse, verified_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.verified_contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: SendblueAPI) -> None:
        verified_contact = client.verified_contacts.list()
        assert_matches_type(VerifiedContactListResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SendblueAPI) -> None:
        response = client.verified_contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_contact = response.parse()
        assert_matches_type(VerifiedContactListResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SendblueAPI) -> None:
        with client.verified_contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_contact = response.parse()
            assert_matches_type(VerifiedContactListResponse, verified_contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerifiedContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSendblueAPI) -> None:
        verified_contact = await async_client.verified_contacts.create(
            phone_number="+12125550199",
        )
        assert_matches_type(VerifiedContactCreateResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.verified_contacts.with_raw_response.create(
            phone_number="+12125550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_contact = await response.parse()
        assert_matches_type(VerifiedContactCreateResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.verified_contacts.with_streaming_response.create(
            phone_number="+12125550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_contact = await response.parse()
            assert_matches_type(VerifiedContactCreateResponse, verified_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        verified_contact = await async_client.verified_contacts.retrieve(
            "+12125550199",
        )
        assert_matches_type(VerifiedContactRetrieveResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.verified_contacts.with_raw_response.retrieve(
            "+12125550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_contact = await response.parse()
        assert_matches_type(VerifiedContactRetrieveResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.verified_contacts.with_streaming_response.retrieve(
            "+12125550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_contact = await response.parse()
            assert_matches_type(VerifiedContactRetrieveResponse, verified_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.verified_contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSendblueAPI) -> None:
        verified_contact = await async_client.verified_contacts.list()
        assert_matches_type(VerifiedContactListResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.verified_contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verified_contact = await response.parse()
        assert_matches_type(VerifiedContactListResponse, verified_contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.verified_contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verified_contact = await response.parse()
            assert_matches_type(VerifiedContactListResponse, verified_contact, path=["response"])

        assert cast(Any, response.is_closed) is True
