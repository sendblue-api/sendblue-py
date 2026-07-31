# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types import (
    MessageResponse,
    MessageListResponse,
    MessageRetrieveResponse,
)
from sendblue_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        message = client.messages.retrieve(
            "msg_abc123def456",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.messages.with_raw_response.retrieve(
            "msg_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.messages.with_streaming_response.retrieve(
            "msg_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: SendblueAPI) -> None:
        message = client.messages.list()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: SendblueAPI) -> None:
        message = client.messages.list(
            account_email="user@example.com",
            created_at_gte=parse_datetime("2024-01-01T00:00:00Z"),
            created_at_lte=parse_datetime("2024-01-31T23:59:59Z"),
            from_number="+19998887777",
            group_id="group_123456",
            is_outbound="true",
            limit=1,
            message_type="message",
            number="+19998887777",
            offset=0,
            order_by="createdAt",
            order_direction="asc",
            sendblue_number="+19998887777",
            sent_at_gte=parse_datetime("2024-01-01T00:00:00Z"),
            sent_at_lte=parse_datetime("2024-01-31T23:59:59Z"),
            service="iMessage",
            status="REGISTERED",
            to_number="+18887776666",
            updated_at_gte=parse_datetime("2024-01-01T00:00:00Z"),
            updated_at_lte=parse_datetime("2024-01-31T23:59:59Z"),
            worker_id="worker_123",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SendblueAPI) -> None:
        response = client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SendblueAPI) -> None:
        with client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: SendblueAPI) -> None:
        message = client.messages.get_status(
            handle="msg_abc123def456",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: SendblueAPI) -> None:
        response = client.messages.with_raw_response.get_status(
            handle="msg_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: SendblueAPI) -> None:
        with client.messages.with_streaming_response.get_status(
            handle="msg_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: SendblueAPI) -> None:
        message = client.messages.send(
            from_number="+19998887777",
            number="+19998887777",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: SendblueAPI) -> None:
        message = client.messages.send(
            from_number="+19998887777",
            number="+19998887777",
            app_card={
                "app_name": "My App",
                "extension_bundle_id": "com.example.myapp.MessagesExtension",
                "layout": {
                    "caption": "Check this out",
                    "image_subtitle": "imageSubtitle",
                    "image_title": "imageTitle",
                    "image_url": "https://example.com",
                    "subcaption": "Tap to open",
                    "summary": "summary",
                    "trailing_caption": "trailingCaption",
                    "trailing_subcaption": "trailingSubcaption",
                },
                "team_id": "ABCDE12345",
                "url": "https://example.com/deep-link",
                "app_store_id": 1234567890,
                "fallback_text": "fallbackText",
                "interactive": True,
                "session_identifier": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            content="Hello, World!",
            media_url="https://example.com/image.jpg",
            reply_to={
                "message_handle": "msg_parent123",
                "part_index": 0,
            },
            seat_id="550e8400-e29b-41d4-a716-446655440000",
            send_style="celebration",
            status_callback="https://example.com/webhook",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: SendblueAPI) -> None:
        response = client.messages.with_raw_response.send(
            from_number="+19998887777",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: SendblueAPI) -> None:
        with client.messages.with_streaming_response.send(
            from_number="+19998887777",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_app_card(self, client: SendblueAPI) -> None:
        message = client.messages.update_app_card(
            message_handle="message_handle",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_app_card_with_all_params(self, client: SendblueAPI) -> None:
        message = client.messages.update_app_card(
            message_handle="message_handle",
            fallback_text="fallback_text",
            idempotency_key="x",
            interactive=True,
            layout={
                "caption": "Check this out",
                "image_subtitle": "imageSubtitle",
                "image_title": "imageTitle",
                "image_url": "https://example.com",
                "subcaption": "Tap to open",
                "summary": "summary",
                "trailing_caption": "trailingCaption",
                "trailing_subcaption": "trailingSubcaption",
            },
            send_style="celebration",
            url="https://example.com",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_app_card(self, client: SendblueAPI) -> None:
        response = client.messages.with_raw_response.update_app_card(
            message_handle="message_handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_app_card(self, client: SendblueAPI) -> None:
        with client.messages.with_streaming_response.update_app_card(
            message_handle="message_handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_app_card(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_handle` but received ''"):
            client.messages.with_raw_response.update_app_card(
                message_handle="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.retrieve(
            "msg_abc123def456",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            "msg_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            "msg_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.list()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.list(
            account_email="user@example.com",
            created_at_gte=parse_datetime("2024-01-01T00:00:00Z"),
            created_at_lte=parse_datetime("2024-01-31T23:59:59Z"),
            from_number="+19998887777",
            group_id="group_123456",
            is_outbound="true",
            limit=1,
            message_type="message",
            number="+19998887777",
            offset=0,
            order_by="createdAt",
            order_direction="asc",
            sendblue_number="+19998887777",
            sent_at_gte=parse_datetime("2024-01-01T00:00:00Z"),
            sent_at_lte=parse_datetime("2024-01-31T23:59:59Z"),
            service="iMessage",
            status="REGISTERED",
            to_number="+18887776666",
            updated_at_gte=parse_datetime("2024-01-01T00:00:00Z"),
            updated_at_lte=parse_datetime("2024-01-31T23:59:59Z"),
            worker_id="worker_123",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.get_status(
            handle="msg_abc123def456",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.messages.with_raw_response.get_status(
            handle="msg_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.messages.with_streaming_response.get_status(
            handle="msg_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.send(
            from_number="+19998887777",
            number="+19998887777",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.send(
            from_number="+19998887777",
            number="+19998887777",
            app_card={
                "app_name": "My App",
                "extension_bundle_id": "com.example.myapp.MessagesExtension",
                "layout": {
                    "caption": "Check this out",
                    "image_subtitle": "imageSubtitle",
                    "image_title": "imageTitle",
                    "image_url": "https://example.com",
                    "subcaption": "Tap to open",
                    "summary": "summary",
                    "trailing_caption": "trailingCaption",
                    "trailing_subcaption": "trailingSubcaption",
                },
                "team_id": "ABCDE12345",
                "url": "https://example.com/deep-link",
                "app_store_id": 1234567890,
                "fallback_text": "fallbackText",
                "interactive": True,
                "session_identifier": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            content="Hello, World!",
            media_url="https://example.com/image.jpg",
            reply_to={
                "message_handle": "msg_parent123",
                "part_index": 0,
            },
            seat_id="550e8400-e29b-41d4-a716-446655440000",
            send_style="celebration",
            status_callback="https://example.com/webhook",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.messages.with_raw_response.send(
            from_number="+19998887777",
            number="+19998887777",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.messages.with_streaming_response.send(
            from_number="+19998887777",
            number="+19998887777",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_app_card(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.update_app_card(
            message_handle="message_handle",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_app_card_with_all_params(self, async_client: AsyncSendblueAPI) -> None:
        message = await async_client.messages.update_app_card(
            message_handle="message_handle",
            fallback_text="fallback_text",
            idempotency_key="x",
            interactive=True,
            layout={
                "caption": "Check this out",
                "image_subtitle": "imageSubtitle",
                "image_title": "imageTitle",
                "image_url": "https://example.com",
                "subcaption": "Tap to open",
                "summary": "summary",
                "trailing_caption": "trailingCaption",
                "trailing_subcaption": "trailingSubcaption",
            },
            send_style="celebration",
            url="https://example.com",
        )
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_app_card(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.messages.with_raw_response.update_app_card(
            message_handle="message_handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_app_card(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.messages.with_streaming_response.update_app_card(
            message_handle="message_handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_app_card(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_handle` but received ''"):
            await async_client.messages.with_raw_response.update_app_card(
                message_handle="",
            )
