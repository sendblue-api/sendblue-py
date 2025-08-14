# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import MessageResponse, GroupModifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_modify(self, client: SendblueAPI) -> None:
        group = client.groups.modify(
            group_id="group_123456",
            modify_type="add_recipient",
            number="+19998887777",
        )
        assert_matches_type(GroupModifyResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_modify(self, client: SendblueAPI) -> None:
        response = client.groups.with_raw_response.modify(
            group_id="group_123456",
            modify_type="add_recipient",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupModifyResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_modify(self, client: SendblueAPI) -> None:
        with client.groups.with_streaming_response.modify(
            group_id="group_123456",
            modify_type="add_recipient",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupModifyResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message(self, client: SendblueAPI) -> None:
        group = client.groups.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
        )
        assert_matches_type(MessageResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: SendblueAPI) -> None:
        group = client.groups.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
            group_id="group_123456",
            media_url="https://example.com/image.jpg",
            numbers=["+19998887777", "+18887776666"],
        )
        assert_matches_type(MessageResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: SendblueAPI) -> None:
        response = client.groups.with_raw_response.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(MessageResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: SendblueAPI) -> None:
        with client.groups.with_streaming_response.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(MessageResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_modify(self, async_client: AsyncSendblueAPI) -> None:
        group = await async_client.groups.modify(
            group_id="group_123456",
            modify_type="add_recipient",
            number="+19998887777",
        )
        assert_matches_type(GroupModifyResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_modify(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.groups.with_raw_response.modify(
            group_id="group_123456",
            modify_type="add_recipient",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupModifyResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_modify(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.groups.with_streaming_response.modify(
            group_id="group_123456",
            modify_type="add_recipient",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupModifyResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncSendblueAPI) -> None:
        group = await async_client.groups.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
        )
        assert_matches_type(MessageResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        group = await async_client.groups.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
            group_id="group_123456",
            media_url="https://example.com/image.jpg",
            numbers=["+19998887777", "+18887776666"],
        )
        assert_matches_type(MessageResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.groups.with_raw_response.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(MessageResponse, group, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.groups.with_streaming_response.send_message(
            content="Hello, everyone!",
            from_number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(MessageResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True
