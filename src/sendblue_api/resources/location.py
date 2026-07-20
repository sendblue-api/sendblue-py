# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import location_list_params, location_watch_params, location_retrieve_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.location_list_response import LocationListResponse
from ..types.location_watch_response import LocationWatchResponse
from ..types.location_retrieve_response import LocationRetrieveResponse

__all__ = ["LocationResource", "AsyncLocationResource"]


class LocationResource(SyncAPIResource):
    """Operations for sending and managing messages"""

    @cached_property
    def with_raw_response(self) -> LocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return LocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return LocationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        number: str,
        *,
        from_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationRetrieveResponse:
        """
        Read the current Find My location for one contact if that contact already shares
        with a dedicated Mac-backed Sendblue number. Shared lines cannot use this
        endpoint.

        Args:
          from_number: Your Sendblue number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        return self._get(
            path_template("/api/location/{number}", number=number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_number": from_number}, location_retrieve_params.LocationRetrieveParams),
            ),
            cast_to=LocationRetrieveResponse,
        )

    def list(
        self,
        *,
        from_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListResponse:
        """
        Read the current Find My locations already shared with a dedicated Mac-backed
        Sendblue number. Shared lines cannot use this endpoint.

        Args:
          from_number: Your Sendblue number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/location",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_number": from_number}, location_list_params.LocationListParams),
            ),
            cast_to=LocationListResponse,
        )

    def watch(
        self,
        number: str,
        *,
        from_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[LocationWatchResponse]:
        """
        Open a Server-Sent Events (SSE) stream for live Find My updates from one contact
        sharing with a dedicated Mac-backed Sendblue number. Shared lines cannot use
        this endpoint.

        The stream has no client-visible duration. It remains open while the client is
        connected, authorized, and the worker is available. Comment heartbeats are sent
        every 15 seconds. Clients should reconnect with their normal credentials after a
        network interruption or a `worker_disconnected` completion. Location events are
        live-only and may repeat across internal native-watch renewals.

        Named events and their JSON `data` payloads:

        - `ready`: the native watch is active.
        - `location`: a location state or fix.
        - `complete`: the watch ended normally. Known reasons are `sharing_ended`,
          `authorization_revoked`, `worker_disconnected`, and `watch_ended`. Clients
          should tolerate additional completion reasons.
        - `error`: the watch failed after the SSE response started.

        Args:
          from_number: Your supported Sendblue number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/api/location/{number}/watch", number=number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"from_number": from_number}, location_watch_params.LocationWatchParams),
            ),
            cast_to=LocationWatchResponse,
            stream=True,
            stream_cls=Stream[LocationWatchResponse],
        )


class AsyncLocationResource(AsyncAPIResource):
    """Operations for sending and managing messages"""

    @cached_property
    def with_raw_response(self) -> AsyncLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncLocationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        number: str,
        *,
        from_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationRetrieveResponse:
        """
        Read the current Find My location for one contact if that contact already shares
        with a dedicated Mac-backed Sendblue number. Shared lines cannot use this
        endpoint.

        Args:
          from_number: Your Sendblue number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        return await self._get(
            path_template("/api/location/{number}", number=number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"from_number": from_number}, location_retrieve_params.LocationRetrieveParams
                ),
            ),
            cast_to=LocationRetrieveResponse,
        )

    async def list(
        self,
        *,
        from_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListResponse:
        """
        Read the current Find My locations already shared with a dedicated Mac-backed
        Sendblue number. Shared lines cannot use this endpoint.

        Args:
          from_number: Your Sendblue number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/location",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"from_number": from_number}, location_list_params.LocationListParams
                ),
            ),
            cast_to=LocationListResponse,
        )

    async def watch(
        self,
        number: str,
        *,
        from_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[LocationWatchResponse]:
        """
        Open a Server-Sent Events (SSE) stream for live Find My updates from one contact
        sharing with a dedicated Mac-backed Sendblue number. Shared lines cannot use
        this endpoint.

        The stream has no client-visible duration. It remains open while the client is
        connected, authorized, and the worker is available. Comment heartbeats are sent
        every 15 seconds. Clients should reconnect with their normal credentials after a
        network interruption or a `worker_disconnected` completion. Location events are
        live-only and may repeat across internal native-watch renewals.

        Named events and their JSON `data` payloads:

        - `ready`: the native watch is active.
        - `location`: a location state or fix.
        - `complete`: the watch ended normally. Known reasons are `sharing_ended`,
          `authorization_revoked`, `worker_disconnected`, and `watch_ended`. Clients
          should tolerate additional completion reasons.
        - `error`: the watch failed after the SSE response started.

        Args:
          from_number: Your supported Sendblue number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/api/location/{number}/watch", number=number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"from_number": from_number}, location_watch_params.LocationWatchParams
                ),
            ),
            cast_to=LocationWatchResponse,
            stream=True,
            stream_cls=AsyncStream[LocationWatchResponse],
        )


class LocationResourceWithRawResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

        self.retrieve = to_raw_response_wrapper(
            location.retrieve,
        )
        self.list = to_raw_response_wrapper(
            location.list,
        )
        self.watch = to_raw_response_wrapper(
            location.watch,
        )


class AsyncLocationResourceWithRawResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

        self.retrieve = async_to_raw_response_wrapper(
            location.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            location.list,
        )
        self.watch = async_to_raw_response_wrapper(
            location.watch,
        )


class LocationResourceWithStreamingResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

        self.retrieve = to_streamed_response_wrapper(
            location.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            location.list,
        )
        self.watch = to_streamed_response_wrapper(
            location.watch,
        )


class AsyncLocationResourceWithStreamingResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

        self.retrieve = async_to_streamed_response_wrapper(
            location.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            location.list,
        )
        self.watch = async_to_streamed_response_wrapper(
            location.watch,
        )
