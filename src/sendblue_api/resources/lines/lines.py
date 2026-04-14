# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .call_forwarding import (
    CallForwardingResource,
    AsyncCallForwardingResource,
    CallForwardingResourceWithRawResponse,
    AsyncCallForwardingResourceWithRawResponse,
    CallForwardingResourceWithStreamingResponse,
    AsyncCallForwardingResourceWithStreamingResponse,
)

__all__ = ["LinesResource", "AsyncLinesResource"]


class LinesResource(SyncAPIResource):
    @cached_property
    def call_forwarding(self) -> CallForwardingResource:
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


class AsyncLinesResource(AsyncAPIResource):
    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResource:
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


class LinesResourceWithRawResponse:
    def __init__(self, lines: LinesResource) -> None:
        self._lines = lines

    @cached_property
    def call_forwarding(self) -> CallForwardingResourceWithRawResponse:
        return CallForwardingResourceWithRawResponse(self._lines.call_forwarding)


class AsyncLinesResourceWithRawResponse:
    def __init__(self, lines: AsyncLinesResource) -> None:
        self._lines = lines

    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResourceWithRawResponse:
        return AsyncCallForwardingResourceWithRawResponse(self._lines.call_forwarding)


class LinesResourceWithStreamingResponse:
    def __init__(self, lines: LinesResource) -> None:
        self._lines = lines

    @cached_property
    def call_forwarding(self) -> CallForwardingResourceWithStreamingResponse:
        return CallForwardingResourceWithStreamingResponse(self._lines.call_forwarding)


class AsyncLinesResourceWithStreamingResponse:
    def __init__(self, lines: AsyncLinesResource) -> None:
        self._lines = lines

    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResourceWithStreamingResponse:
        return AsyncCallForwardingResourceWithStreamingResponse(self._lines.call_forwarding)
