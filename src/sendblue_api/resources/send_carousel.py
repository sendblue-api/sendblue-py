# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import send_carousel_send_params
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
from ..types.send_carousel_send_response import SendCarouselSendResponse

__all__ = ["SendCarouselResource", "AsyncSendCarouselResource"]


class SendCarouselResource(SyncAPIResource):
    """Operations for sending and managing messages"""

    @cached_property
    def with_raw_response(self) -> SendCarouselResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return SendCarouselResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendCarouselResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return SendCarouselResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        from_number: str,
        media_urls: SequenceNotStr[str],
        number: str,
        metadata: object | Omit = omit,
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
    ) -> SendCarouselSendResponse:
        """Send a carousel of images to a single recipient.

        Requires a V2 (Mac Mini) line.
        The carousel must contain between 2 and 20 HTTPS image URLs. For sending a
        single image, use `/api/send-message` with `media_url` instead.

        Args:
          from_number: Your Sendblue phone number in E.164 format (must be a V2/Mac Mini line)

          media_urls: Array of HTTPS image URLs to send as a carousel (2-20 items)

          number: Recipient phone number in E.164 format

          metadata: Additional metadata to attach to the message

          send_style: The iMessage expressive message style

          status_callback: Webhook URL for message status updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/send-carousel",
            body=maybe_transform(
                {
                    "from_number": from_number,
                    "media_urls": media_urls,
                    "number": number,
                    "metadata": metadata,
                    "send_style": send_style,
                    "status_callback": status_callback,
                },
                send_carousel_send_params.SendCarouselSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendCarouselSendResponse,
        )


class AsyncSendCarouselResource(AsyncAPIResource):
    """Operations for sending and managing messages"""

    @cached_property
    def with_raw_response(self) -> AsyncSendCarouselResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSendCarouselResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendCarouselResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncSendCarouselResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        from_number: str,
        media_urls: SequenceNotStr[str],
        number: str,
        metadata: object | Omit = omit,
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
    ) -> SendCarouselSendResponse:
        """Send a carousel of images to a single recipient.

        Requires a V2 (Mac Mini) line.
        The carousel must contain between 2 and 20 HTTPS image URLs. For sending a
        single image, use `/api/send-message` with `media_url` instead.

        Args:
          from_number: Your Sendblue phone number in E.164 format (must be a V2/Mac Mini line)

          media_urls: Array of HTTPS image URLs to send as a carousel (2-20 items)

          number: Recipient phone number in E.164 format

          metadata: Additional metadata to attach to the message

          send_style: The iMessage expressive message style

          status_callback: Webhook URL for message status updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/send-carousel",
            body=await async_maybe_transform(
                {
                    "from_number": from_number,
                    "media_urls": media_urls,
                    "number": number,
                    "metadata": metadata,
                    "send_style": send_style,
                    "status_callback": status_callback,
                },
                send_carousel_send_params.SendCarouselSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendCarouselSendResponse,
        )


class SendCarouselResourceWithRawResponse:
    def __init__(self, send_carousel: SendCarouselResource) -> None:
        self._send_carousel = send_carousel

        self.send = to_raw_response_wrapper(
            send_carousel.send,
        )


class AsyncSendCarouselResourceWithRawResponse:
    def __init__(self, send_carousel: AsyncSendCarouselResource) -> None:
        self._send_carousel = send_carousel

        self.send = async_to_raw_response_wrapper(
            send_carousel.send,
        )


class SendCarouselResourceWithStreamingResponse:
    def __init__(self, send_carousel: SendCarouselResource) -> None:
        self._send_carousel = send_carousel

        self.send = to_streamed_response_wrapper(
            send_carousel.send,
        )


class AsyncSendCarouselResourceWithStreamingResponse:
    def __init__(self, send_carousel: AsyncSendCarouselResource) -> None:
        self._send_carousel = send_carousel

        self.send = async_to_streamed_response_wrapper(
            send_carousel.send,
        )
