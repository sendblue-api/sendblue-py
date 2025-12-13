# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import message_list_params, message_send_params, message_get_status_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.message_response import MessageResponse
from ..types.message_list_response import MessageListResponse
from ..types.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieve details of a specific message by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/api/v2/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def list(
        self,
        *,
        account_email: str | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        from_number: str | Omit = omit,
        group_id: str | Omit = omit,
        is_outbound: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        message_type: Literal["message", "group"] | Omit = omit,
        number: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["createdAt", "updatedAt", "sentAt"] | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        sendblue_number: str | Omit = omit,
        sent_at_gte: Union[str, datetime] | Omit = omit,
        sent_at_lte: Union[str, datetime] | Omit = omit,
        service: Literal["iMessage", "SMS"] | Omit = omit,
        status: Literal[
            "REGISTERED",
            "PENDING",
            "SENT",
            "DELIVERED",
            "RECEIVED",
            "QUEUED",
            "ERROR",
            "DECLINED",
            "ACCEPTED",
            "SUCCESS",
        ]
        | Omit = omit,
        to_number: str | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        worker_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Retrieve a list of messages for the authenticated account with comprehensive
        filtering capabilities. Rate limited to 100 requests per 10 seconds per account.

        Args:
          account_email: Filter by account email

          created_at_gte: Filter messages created after this date (ISO 8601 format)

          created_at_lte: Filter messages created before this date (ISO 8601 format)

          from_number: Filter by sender phone number

          group_id: Filter by group ID

          is_outbound: Filter by message direction

          limit: Maximum number of messages to return

          message_type: Filter by message type

          number: Filter by any phone number (from or to)

          offset: Number of messages to skip

          order_by: Field to order messages by

          order_direction: Sort order

          sendblue_number: Filter by Sendblue phone number

          sent_at_gte: Filter messages sent after this date (ISO 8601 format)

          sent_at_lte: Filter messages sent before this date (ISO 8601 format)

          service: Filter by service type

          status: Filter by message status

          to_number: Filter by recipient phone number

          updated_at_gte: Filter messages updated after this date (ISO 8601 format)

          updated_at_lte: Filter messages updated before this date (ISO 8601 format)

          worker_id: Filter by worker ID (Admin only)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_email": account_email,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "from_number": from_number,
                        "group_id": group_id,
                        "is_outbound": is_outbound,
                        "limit": limit,
                        "message_type": message_type,
                        "number": number,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "sendblue_number": sendblue_number,
                        "sent_at_gte": sent_at_gte,
                        "sent_at_lte": sent_at_lte,
                        "service": service,
                        "status": status,
                        "to_number": to_number,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                        "worker_id": worker_id,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def get_status(
        self,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """Retrieve the current status of a message using its message handle.

        Useful for
        resolving pending message statuses and avoiding duplicate messages.

        Args:
          handle: The message handle of the message you want to check status for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"handle": handle}, message_get_status_params.MessageGetStatusParams),
            ),
            cast_to=MessageResponse,
        )

    def send(
        self,
        *,
        content: str,
        from_number: str,
        number: str,
        media_url: str | Omit = omit,
        send_style: Literal[
            "celebration",
            "shooting_star",
            "fireworks",
            "lasers",
            "love",
            "confetti",
            "balloons",
            "spotlight",
            "echo",
            "invisible",
            "gentle",
            "loud",
            "slam",
        ]
        | Omit = omit,
        status_callback: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Send an iMessage, SMS, or MMS to a single recipient

        Args:
          content: Message text content

          from_number: **REQUIRED** - The phone number to send from. Must be one of your registered
              Sendblue phone numbers in E.164 format. Without this parameter, the message will
              fail to send.

          number: Recipient phone number in E.164 format

          media_url: URL of media file to send (images, videos, etc.)

          send_style: The iMessage expressive message style

          status_callback: Webhook URL for message status updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/send-message",
            body=maybe_transform(
                {
                    "content": content,
                    "from_number": from_number,
                    "number": number,
                    "media_url": media_url,
                    "send_style": send_style,
                    "status_callback": status_callback,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieve details of a specific message by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/api/v2/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_email: str | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        from_number: str | Omit = omit,
        group_id: str | Omit = omit,
        is_outbound: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        message_type: Literal["message", "group"] | Omit = omit,
        number: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["createdAt", "updatedAt", "sentAt"] | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        sendblue_number: str | Omit = omit,
        sent_at_gte: Union[str, datetime] | Omit = omit,
        sent_at_lte: Union[str, datetime] | Omit = omit,
        service: Literal["iMessage", "SMS"] | Omit = omit,
        status: Literal[
            "REGISTERED",
            "PENDING",
            "SENT",
            "DELIVERED",
            "RECEIVED",
            "QUEUED",
            "ERROR",
            "DECLINED",
            "ACCEPTED",
            "SUCCESS",
        ]
        | Omit = omit,
        to_number: str | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        worker_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Retrieve a list of messages for the authenticated account with comprehensive
        filtering capabilities. Rate limited to 100 requests per 10 seconds per account.

        Args:
          account_email: Filter by account email

          created_at_gte: Filter messages created after this date (ISO 8601 format)

          created_at_lte: Filter messages created before this date (ISO 8601 format)

          from_number: Filter by sender phone number

          group_id: Filter by group ID

          is_outbound: Filter by message direction

          limit: Maximum number of messages to return

          message_type: Filter by message type

          number: Filter by any phone number (from or to)

          offset: Number of messages to skip

          order_by: Field to order messages by

          order_direction: Sort order

          sendblue_number: Filter by Sendblue phone number

          sent_at_gte: Filter messages sent after this date (ISO 8601 format)

          sent_at_lte: Filter messages sent before this date (ISO 8601 format)

          service: Filter by service type

          status: Filter by message status

          to_number: Filter by recipient phone number

          updated_at_gte: Filter messages updated after this date (ISO 8601 format)

          updated_at_lte: Filter messages updated before this date (ISO 8601 format)

          worker_id: Filter by worker ID (Admin only)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_email": account_email,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "from_number": from_number,
                        "group_id": group_id,
                        "is_outbound": is_outbound,
                        "limit": limit,
                        "message_type": message_type,
                        "number": number,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "sendblue_number": sendblue_number,
                        "sent_at_gte": sent_at_gte,
                        "sent_at_lte": sent_at_lte,
                        "service": service,
                        "status": status,
                        "to_number": to_number,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                        "worker_id": worker_id,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def get_status(
        self,
        *,
        handle: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """Retrieve the current status of a message using its message handle.

        Useful for
        resolving pending message statuses and avoiding duplicate messages.

        Args:
          handle: The message handle of the message you want to check status for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"handle": handle}, message_get_status_params.MessageGetStatusParams),
            ),
            cast_to=MessageResponse,
        )

    async def send(
        self,
        *,
        content: str,
        from_number: str,
        number: str,
        media_url: str | Omit = omit,
        send_style: Literal[
            "celebration",
            "shooting_star",
            "fireworks",
            "lasers",
            "love",
            "confetti",
            "balloons",
            "spotlight",
            "echo",
            "invisible",
            "gentle",
            "loud",
            "slam",
        ]
        | Omit = omit,
        status_callback: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Send an iMessage, SMS, or MMS to a single recipient

        Args:
          content: Message text content

          from_number: **REQUIRED** - The phone number to send from. Must be one of your registered
              Sendblue phone numbers in E.164 format. Without this parameter, the message will
              fail to send.

          number: Recipient phone number in E.164 format

          media_url: URL of media file to send (images, videos, etc.)

          send_style: The iMessage expressive message style

          status_callback: Webhook URL for message status updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/send-message",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "from_number": from_number,
                    "number": number,
                    "media_url": media_url,
                    "send_style": send_style,
                    "status_callback": status_callback,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.get_status = to_raw_response_wrapper(
            messages.get_status,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.get_status = async_to_raw_response_wrapper(
            messages.get_status,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.get_status = to_streamed_response_wrapper(
            messages.get_status,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.get_status = async_to_streamed_response_wrapper(
            messages.get_status,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
