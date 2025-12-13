# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import typing_indicator_send_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.typing_indicator_send_response import TypingIndicatorSendResponse

__all__ = ["TypingIndicatorsResource", "AsyncTypingIndicatorsResource"]


class TypingIndicatorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TypingIndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return TypingIndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypingIndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return TypingIndicatorsResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        from_number: str,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypingIndicatorSendResponse:
        """Send an indication that you are typing to a user.

        This shows up as the animated
        three dots on the recipient's device. Not supported in group chats.

        Args:
          from_number: The Sendblue phone number you want to send the typing indicator from (E.164
              format). This should be the number you use to send messages.

          number: The number you want to send a typing indicator to (E.164 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/send-typing-indicator",
            body=maybe_transform(
                {
                    "from_number": from_number,
                    "number": number,
                },
                typing_indicator_send_params.TypingIndicatorSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypingIndicatorSendResponse,
        )


class AsyncTypingIndicatorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTypingIndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTypingIndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypingIndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncTypingIndicatorsResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        from_number: str,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TypingIndicatorSendResponse:
        """Send an indication that you are typing to a user.

        This shows up as the animated
        three dots on the recipient's device. Not supported in group chats.

        Args:
          from_number: The Sendblue phone number you want to send the typing indicator from (E.164
              format). This should be the number you use to send messages.

          number: The number you want to send a typing indicator to (E.164 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/send-typing-indicator",
            body=await async_maybe_transform(
                {
                    "from_number": from_number,
                    "number": number,
                },
                typing_indicator_send_params.TypingIndicatorSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TypingIndicatorSendResponse,
        )


class TypingIndicatorsResourceWithRawResponse:
    def __init__(self, typing_indicators: TypingIndicatorsResource) -> None:
        self._typing_indicators = typing_indicators

        self.send = to_raw_response_wrapper(
            typing_indicators.send,
        )


class AsyncTypingIndicatorsResourceWithRawResponse:
    def __init__(self, typing_indicators: AsyncTypingIndicatorsResource) -> None:
        self._typing_indicators = typing_indicators

        self.send = async_to_raw_response_wrapper(
            typing_indicators.send,
        )


class TypingIndicatorsResourceWithStreamingResponse:
    def __init__(self, typing_indicators: TypingIndicatorsResource) -> None:
        self._typing_indicators = typing_indicators

        self.send = to_streamed_response_wrapper(
            typing_indicators.send,
        )


class AsyncTypingIndicatorsResourceWithStreamingResponse:
    def __init__(self, typing_indicators: AsyncTypingIndicatorsResource) -> None:
        self._typing_indicators = typing_indicators

        self.send = async_to_streamed_response_wrapper(
            typing_indicators.send,
        )
