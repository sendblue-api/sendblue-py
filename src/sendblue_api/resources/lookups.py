# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import lookup_lookup_number_params
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
from ..types.lookup_lookup_number_response import LookupLookupNumberResponse

__all__ = ["LookupsResource", "AsyncLookupsResource"]


class LookupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LookupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return LookupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return LookupsResourceWithStreamingResponse(self)

    def lookup_number(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupLookupNumberResponse:
        """Determine if a phone number supports iMessage or SMS.

        Useful for checking if a
        number is an iPhone, if it is real, or which provider to use.

        Args:
          number: The number you want to evaluate in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/evaluate-service",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"number": number}, lookup_lookup_number_params.LookupLookupNumberParams),
            ),
            cast_to=LookupLookupNumberResponse,
        )


class AsyncLookupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLookupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLookupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncLookupsResourceWithStreamingResponse(self)

    async def lookup_number(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupLookupNumberResponse:
        """Determine if a phone number supports iMessage or SMS.

        Useful for checking if a
        number is an iPhone, if it is real, or which provider to use.

        Args:
          number: The number you want to evaluate in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/evaluate-service",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"number": number}, lookup_lookup_number_params.LookupLookupNumberParams
                ),
            ),
            cast_to=LookupLookupNumberResponse,
        )


class LookupsResourceWithRawResponse:
    def __init__(self, lookups: LookupsResource) -> None:
        self._lookups = lookups

        self.lookup_number = to_raw_response_wrapper(
            lookups.lookup_number,
        )


class AsyncLookupsResourceWithRawResponse:
    def __init__(self, lookups: AsyncLookupsResource) -> None:
        self._lookups = lookups

        self.lookup_number = async_to_raw_response_wrapper(
            lookups.lookup_number,
        )


class LookupsResourceWithStreamingResponse:
    def __init__(self, lookups: LookupsResource) -> None:
        self._lookups = lookups

        self.lookup_number = to_streamed_response_wrapper(
            lookups.lookup_number,
        )


class AsyncLookupsResourceWithStreamingResponse:
    def __init__(self, lookups: AsyncLookupsResource) -> None:
        self._lookups = lookups

        self.lookup_number = async_to_streamed_response_wrapper(
            lookups.lookup_number,
        )
