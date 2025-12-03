# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import group_modify_params, group_send_message_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.group_modify_response import GroupModifyResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def modify(
        self,
        *,
        group_id: str,
        modify_type: Literal["add_recipient"],
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupModifyResponse:
        """
        Add or manage participants in a group chat (beta feature)

        Args:
          group_id: Group identifier

          modify_type: Type of modification to perform

          number: Phone number to add/modify in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/modify-group",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "modify_type": modify_type,
                    "number": number,
                },
                group_modify_params.GroupModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupModifyResponse,
        )

    def send_message(
        self,
        *,
        content: str,
        from_number: str,
        group_id: str | Omit = omit,
        media_url: str | Omit = omit,
        numbers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Send a message to a group of recipients (beta feature)

        Args:
          content: Message text content

          from_number: **REQUIRED** - The phone number to send from. Must be one of your registered
              Sendblue phone numbers in E.164 format. Without this parameter, the message will
              fail to send.

          group_id: Unique identifier for an existing group

          media_url: URL of media file to send

          numbers: Array of recipient phone numbers in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/send-group-message",
            body=maybe_transform(
                {
                    "content": content,
                    "from_number": from_number,
                    "group_id": group_id,
                    "media_url": media_url,
                    "numbers": numbers,
                },
                group_send_message_params.GroupSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def modify(
        self,
        *,
        group_id: str,
        modify_type: Literal["add_recipient"],
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupModifyResponse:
        """
        Add or manage participants in a group chat (beta feature)

        Args:
          group_id: Group identifier

          modify_type: Type of modification to perform

          number: Phone number to add/modify in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/modify-group",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "modify_type": modify_type,
                    "number": number,
                },
                group_modify_params.GroupModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupModifyResponse,
        )

    async def send_message(
        self,
        *,
        content: str,
        from_number: str,
        group_id: str | Omit = omit,
        media_url: str | Omit = omit,
        numbers: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageResponse:
        """
        Send a message to a group of recipients (beta feature)

        Args:
          content: Message text content

          from_number: **REQUIRED** - The phone number to send from. Must be one of your registered
              Sendblue phone numbers in E.164 format. Without this parameter, the message will
              fail to send.

          group_id: Unique identifier for an existing group

          media_url: URL of media file to send

          numbers: Array of recipient phone numbers in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/send-group-message",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "from_number": from_number,
                    "group_id": group_id,
                    "media_url": media_url,
                    "numbers": numbers,
                },
                group_send_message_params.GroupSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageResponse,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.modify = to_raw_response_wrapper(
            groups.modify,
        )
        self.send_message = to_raw_response_wrapper(
            groups.send_message,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.modify = async_to_raw_response_wrapper(
            groups.modify,
        )
        self.send_message = async_to_raw_response_wrapper(
            groups.send_message,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.modify = to_streamed_response_wrapper(
            groups.modify,
        )
        self.send_message = to_streamed_response_wrapper(
            groups.send_message,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.modify = async_to_streamed_response_wrapper(
            groups.modify,
        )
        self.send_message = async_to_streamed_response_wrapper(
            groups.send_message,
        )
