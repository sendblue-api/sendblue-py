# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import event_stream_params
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
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.account_event import AccountEvent

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """Authenticated live account events and recovery contracts"""

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        types: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[AccountEvent]:
        """
        Opens an authenticated Server-Sent Events stream scoped exclusively to the
        account resolved by the supplied credentials. The stream is live and
        intentionally not a durable replay log. It sends a heartbeat every 15 seconds
        and rotates after at most 15 minutes. A temporary-token stream closes no later
        than that token's `expires_at`; clients should reconnect and repair gaps via:

        - `GET /api/v2/messages?updated_at_gte=...&order_by=updated_at&order_direction=asc`
        - `GET /api/v2/contacts?created_at_gte=...&order_by=created_at&order_direction=asc`
        - `GET /api/v2/lines/state`
        - `GET /api/v2/verify/verifications?updated_at_gte=...`

        Each event contains a stable `id`, a `type`, `occurred_at`, and a minimal `data`
        object. Consumers must deduplicate by ID. Typing indicators are ephemeral and
        cannot be recovered.

        Args:
          types: Optional comma-separated allowlist of event types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            "/api/v2/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"types": types}, event_stream_params.EventStreamParams),
            ),
            cast_to=AccountEvent,
            stream=True,
            stream_cls=Stream[AccountEvent],
        )


class AsyncEventsResource(AsyncAPIResource):
    """Authenticated live account events and recovery contracts"""

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        types: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[AccountEvent]:
        """
        Opens an authenticated Server-Sent Events stream scoped exclusively to the
        account resolved by the supplied credentials. The stream is live and
        intentionally not a durable replay log. It sends a heartbeat every 15 seconds
        and rotates after at most 15 minutes. A temporary-token stream closes no later
        than that token's `expires_at`; clients should reconnect and repair gaps via:

        - `GET /api/v2/messages?updated_at_gte=...&order_by=updated_at&order_direction=asc`
        - `GET /api/v2/contacts?created_at_gte=...&order_by=created_at&order_direction=asc`
        - `GET /api/v2/lines/state`
        - `GET /api/v2/verify/verifications?updated_at_gte=...`

        Each event contains a stable `id`, a `type`, `occurred_at`, and a minimal `data`
        object. Consumers must deduplicate by ID. Typing indicators are ephemeral and
        cannot be recovered.

        Args:
          types: Optional comma-separated allowlist of event types

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            "/api/v2/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"types": types}, event_stream_params.EventStreamParams),
            ),
            cast_to=AccountEvent,
            stream=True,
            stream_cls=AsyncStream[AccountEvent],
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.stream = to_raw_response_wrapper(
            events.stream,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.stream = async_to_raw_response_wrapper(
            events.stream,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.stream = to_streamed_response_wrapper(
            events.stream,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.stream = async_to_streamed_response_wrapper(
            events.stream,
        )
