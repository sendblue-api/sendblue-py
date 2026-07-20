# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import request_location_create_params
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
from ..types.request_location_create_response import RequestLocationCreateResponse

__all__ = ["RequestLocationResource", "AsyncRequestLocationResource"]


class RequestLocationResource(SyncAPIResource):
    """Operations for sending and managing messages"""

    @cached_property
    def with_raw_response(self) -> RequestLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return RequestLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return RequestLocationResourceWithStreamingResponse(self)

    def create(
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
    ) -> RequestLocationCreateResponse:
        """
        Send a Find My location request to an iMessage recipient from a dedicated
        Mac-backed Sendblue line. Shared lines cannot initiate location sharing. The
        request is queued like a normal outbound iMessage. If the recipient accepts and
        shares, the location is delivered later as an inbound `message_type: location`
        webhook. Passive inbound location webhooks remain available on shared lines as
        part of the iMessage conversation.

        Args:
          from_number: Your supported Sendblue number in E.164 format

          number: Recipient phone number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/request-location",
            body=maybe_transform(
                {
                    "from_number": from_number,
                    "number": number,
                },
                request_location_create_params.RequestLocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestLocationCreateResponse,
        )


class AsyncRequestLocationResource(AsyncAPIResource):
    """Operations for sending and managing messages"""

    @cached_property
    def with_raw_response(self) -> AsyncRequestLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncRequestLocationResourceWithStreamingResponse(self)

    async def create(
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
    ) -> RequestLocationCreateResponse:
        """
        Send a Find My location request to an iMessage recipient from a dedicated
        Mac-backed Sendblue line. Shared lines cannot initiate location sharing. The
        request is queued like a normal outbound iMessage. If the recipient accepts and
        shares, the location is delivered later as an inbound `message_type: location`
        webhook. Passive inbound location webhooks remain available on shared lines as
        part of the iMessage conversation.

        Args:
          from_number: Your supported Sendblue number in E.164 format

          number: Recipient phone number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/request-location",
            body=await async_maybe_transform(
                {
                    "from_number": from_number,
                    "number": number,
                },
                request_location_create_params.RequestLocationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestLocationCreateResponse,
        )


class RequestLocationResourceWithRawResponse:
    def __init__(self, request_location: RequestLocationResource) -> None:
        self._request_location = request_location

        self.create = to_raw_response_wrapper(
            request_location.create,
        )


class AsyncRequestLocationResourceWithRawResponse:
    def __init__(self, request_location: AsyncRequestLocationResource) -> None:
        self._request_location = request_location

        self.create = async_to_raw_response_wrapper(
            request_location.create,
        )


class RequestLocationResourceWithStreamingResponse:
    def __init__(self, request_location: RequestLocationResource) -> None:
        self._request_location = request_location

        self.create = to_streamed_response_wrapper(
            request_location.create,
        )


class AsyncRequestLocationResourceWithStreamingResponse:
    def __init__(self, request_location: AsyncRequestLocationResource) -> None:
        self._request_location = request_location

        self.create = async_to_streamed_response_wrapper(
            request_location.create,
        )
