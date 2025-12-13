# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import (
    ContactListResponse,
    ContactCountResponse,
    ContactCreateResponse,
    ContactDeleteResponse,
    ContactUpdateResponse,
    ContactVerifyResponse,
    ContactRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: SendblueAPI) -> None:
        contact = client.contacts.create(
            number="number",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: SendblueAPI) -> None:
        contact = client.contacts.create(
            number="number",
            body_assigned_to_email_1="assigned_to_email",
            body_assigned_to_email_2="assignedToEmail",
            body_first_name_1="first_name",
            body_first_name_2="firstName",
            body_last_name_1="last_name",
            body_last_name_2="lastName",
            body_phone_number_1="phone_number",
            body_phone_number_2="phoneNumber",
            body_sendblue_number_1="sendblue_number",
            body_sendblue_number_2="sendblueNumber",
            tags=["string"],
            update_if_exists=True,
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.create(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.create(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        contact = client.contacts.retrieve(
            "+1234567890",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.retrieve(
            "+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.retrieve(
            "+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: SendblueAPI) -> None:
        contact = client.contacts.update(
            phone_number="+1234567890",
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: SendblueAPI) -> None:
        contact = client.contacts.update(
            phone_number="+1234567890",
            body_assigned_to_email_1="assigned_to_email",
            body_assigned_to_email_2="assignedToEmail",
            body_company_name_1="company_name",
            body_company_name_2="companyName",
            body_first_name_1="first_name",
            body_first_name_2="firstName",
            body_last_name_1="last_name",
            body_last_name_2="lastName",
            body_sendblue_number_1="sendblue_number",
            body_sendblue_number_2="sendblueNumber",
            tags=["string"],
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.update(
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.update(
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactUpdateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.contacts.with_raw_response.update(
                phone_number="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: SendblueAPI) -> None:
        contact = client.contacts.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: SendblueAPI) -> None:
        contact = client.contacts.list(
            cid="cid",
            limit=0,
            offset=0,
            order_by="order_by",
            order_direction="asc",
            phone_number="phone_number",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: SendblueAPI) -> None:
        contact = client.contacts.delete(
            "+1234567890",
        )
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.delete(
            "+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.delete(
            "+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactDeleteResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_count(self, client: SendblueAPI) -> None:
        contact = client.contacts.count()
        assert_matches_type(ContactCountResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCountResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCountResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify(self, client: SendblueAPI) -> None:
        contact = client.contacts.verify(
            number="number",
        )
        assert_matches_type(ContactVerifyResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: SendblueAPI) -> None:
        response = client.contacts.with_raw_response.verify(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactVerifyResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: SendblueAPI) -> None:
        with client.contacts.with_streaming_response.verify(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactVerifyResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.create(
            number="number",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.create(
            number="number",
            body_assigned_to_email_1="assigned_to_email",
            body_assigned_to_email_2="assignedToEmail",
            body_first_name_1="first_name",
            body_first_name_2="firstName",
            body_last_name_1="last_name",
            body_last_name_2="lastName",
            body_phone_number_1="phone_number",
            body_phone_number_2="phoneNumber",
            body_sendblue_number_1="sendblue_number",
            body_sendblue_number_2="sendblueNumber",
            tags=["string"],
            update_if_exists=True,
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.create(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.create(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.retrieve(
            "+1234567890",
        )
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.retrieve(
            "+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.retrieve(
            "+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactRetrieveResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.contacts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.update(
            phone_number="+1234567890",
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.update(
            phone_number="+1234567890",
            body_assigned_to_email_1="assigned_to_email",
            body_assigned_to_email_2="assignedToEmail",
            body_company_name_1="company_name",
            body_company_name_2="companyName",
            body_first_name_1="first_name",
            body_first_name_2="firstName",
            body_last_name_1="last_name",
            body_last_name_2="lastName",
            body_sendblue_number_1="sendblue_number",
            body_sendblue_number_2="sendblueNumber",
            tags=["string"],
        )
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.update(
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactUpdateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.update(
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactUpdateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.contacts.with_raw_response.update(
                phone_number="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.list(
            cid="cid",
            limit=0,
            offset=0,
            order_by="order_by",
            order_direction="asc",
            phone_number="phone_number",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.delete(
            "+1234567890",
        )
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.delete(
            "+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.delete(
            "+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactDeleteResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.count()
        assert_matches_type(ContactCountResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCountResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCountResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncSendblueAPI) -> None:
        contact = await async_client.contacts.verify(
            number="number",
        )
        assert_matches_type(ContactVerifyResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.contacts.with_raw_response.verify(
            number="number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactVerifyResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.contacts.with_streaming_response.verify(
            number="number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactVerifyResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
