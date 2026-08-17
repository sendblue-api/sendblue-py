# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .call_forwarding import (
    CallForwardingResource,
    AsyncCallForwardingResource,
    CallForwardingResourceWithRawResponse,
    AsyncCallForwardingResourceWithRawResponse,
    CallForwardingResourceWithStreamingResponse,
    AsyncCallForwardingResourceWithStreamingResponse,
)
from ...types.line_get_state_response import LineGetStateResponse

__all__ = ["LinesResource", "AsyncLinesResource"]


class LinesResource(SyncAPIResource):
    """Sendblue line configuration and health state"""

    @cached_property
    def call_forwarding(self) -> CallForwardingResource:
        """Sendblue line configuration and health state"""
        return CallForwardingResource(self._client)

    @cached_property
    def with_raw_response(self) -> LinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return LinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return LinesResourceWithStreamingResponse(self)

    def get_state(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LineGetStateResponse:
        """
        Returns the authenticated account's current line membership and latest persisted
        health transition.
        """
        return self._get(
            "/api/v2/lines/state",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LineGetStateResponse,
        )


class AsyncLinesResource(AsyncAPIResource):
    """Sendblue line configuration and health state"""

    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResource:
        """Sendblue line configuration and health state"""
        return AsyncCallForwardingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncLinesResourceWithStreamingResponse(self)

    async def get_state(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LineGetStateResponse:
        """
        Returns the authenticated account's current line membership and latest persisted
        health transition.
        """
        return await self._get(
            "/api/v2/lines/state",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LineGetStateResponse,
        )


class LinesResourceWithRawResponse:
    def __init__(self, lines: LinesResource) -> None:
        self._lines = lines

        self.get_state = to_raw_response_wrapper(
            lines.get_state,
        )

    @cached_property
    def call_forwarding(self) -> CallForwardingResourceWithRawResponse:
        """Sendblue line configuration and health state"""
        return CallForwardingResourceWithRawResponse(self._lines.call_forwarding)


class AsyncLinesResourceWithRawResponse:
    def __init__(self, lines: AsyncLinesResource) -> None:
        self._lines = lines

        self.get_state = async_to_raw_response_wrapper(
            lines.get_state,
        )

    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResourceWithRawResponse:
        """Sendblue line configuration and health state"""
        return AsyncCallForwardingResourceWithRawResponse(self._lines.call_forwarding)


class LinesResourceWithStreamingResponse:
    def __init__(self, lines: LinesResource) -> None:
        self._lines = lines

        self.get_state = to_streamed_response_wrapper(
            lines.get_state,
        )

    @cached_property
    def call_forwarding(self) -> CallForwardingResourceWithStreamingResponse:
        """Sendblue line configuration and health state"""
        return CallForwardingResourceWithStreamingResponse(self._lines.call_forwarding)


class AsyncLinesResourceWithStreamingResponse:
    def __init__(self, lines: AsyncLinesResource) -> None:
        self._lines = lines

        self.get_state = async_to_streamed_response_wrapper(
            lines.get_state,
        )

    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResourceWithStreamingResponse:
        """Sendblue line configuration and health state"""
        return AsyncCallForwardingResourceWithStreamingResponse(self._lines.call_forwarding)
