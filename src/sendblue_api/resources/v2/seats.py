# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import seat_list_params, seat_count_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.seat_list_response import SeatListResponse
from ...types.v2.seat_count_response import SeatCountResponse
from ...types.v2.seat_retrieve_response import SeatRetrieveResponse

__all__ = ["SeatsResource", "AsyncSeatsResource"]


class SeatsResource(SyncAPIResource):
    """
    Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
    """

    @cached_property
    def with_raw_response(self) -> SeatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return SeatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return SeatsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        seat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeatRetrieveResponse:
        """Retrieve a single seat by either its UUID or its Firebase Auth subject.

        Both
        identifiers resolve to the same seat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not seat_id:
            raise ValueError(f"Expected a non-empty value for `seat_id` but received {seat_id!r}")
        return self._get(
            path_template("/api/v2/seats/{seat_id}", seat_id=seat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeatRetrieveResponse,
        )

    def list(
        self,
        *,
        email: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeatListResponse:
        """Retrieve a list of seats (users) for the authenticated company.

        Use the returned
        `seat_id` values when sending messages with the `seat_id` parameter to attribute
        activity to a specific rep.

        Args:
          email: Optional exact-match filter on seat email

          limit: Maximum number of seats to return

          offset: Number of seats to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/seats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "limit": limit,
                        "offset": offset,
                    },
                    seat_list_params.SeatListParams,
                ),
            ),
            cast_to=SeatListResponse,
        )

    def count(
        self,
        *,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeatCountResponse:
        """
        Returns the number of seats for the authenticated company.

        Args:
          email: Optional exact-match filter on seat email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/seats/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"email": email}, seat_count_params.SeatCountParams),
            ),
            cast_to=SeatCountResponse,
        )


class AsyncSeatsResource(AsyncAPIResource):
    """
    Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
    """

    @cached_property
    def with_raw_response(self) -> AsyncSeatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSeatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncSeatsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        seat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeatRetrieveResponse:
        """Retrieve a single seat by either its UUID or its Firebase Auth subject.

        Both
        identifiers resolve to the same seat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not seat_id:
            raise ValueError(f"Expected a non-empty value for `seat_id` but received {seat_id!r}")
        return await self._get(
            path_template("/api/v2/seats/{seat_id}", seat_id=seat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SeatRetrieveResponse,
        )

    async def list(
        self,
        *,
        email: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeatListResponse:
        """Retrieve a list of seats (users) for the authenticated company.

        Use the returned
        `seat_id` values when sending messages with the `seat_id` parameter to attribute
        activity to a specific rep.

        Args:
          email: Optional exact-match filter on seat email

          limit: Maximum number of seats to return

          offset: Number of seats to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/seats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "limit": limit,
                        "offset": offset,
                    },
                    seat_list_params.SeatListParams,
                ),
            ),
            cast_to=SeatListResponse,
        )

    async def count(
        self,
        *,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SeatCountResponse:
        """
        Returns the number of seats for the authenticated company.

        Args:
          email: Optional exact-match filter on seat email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/seats/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"email": email}, seat_count_params.SeatCountParams),
            ),
            cast_to=SeatCountResponse,
        )


class SeatsResourceWithRawResponse:
    def __init__(self, seats: SeatsResource) -> None:
        self._seats = seats

        self.retrieve = to_raw_response_wrapper(
            seats.retrieve,
        )
        self.list = to_raw_response_wrapper(
            seats.list,
        )
        self.count = to_raw_response_wrapper(
            seats.count,
        )


class AsyncSeatsResourceWithRawResponse:
    def __init__(self, seats: AsyncSeatsResource) -> None:
        self._seats = seats

        self.retrieve = async_to_raw_response_wrapper(
            seats.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            seats.list,
        )
        self.count = async_to_raw_response_wrapper(
            seats.count,
        )


class SeatsResourceWithStreamingResponse:
    def __init__(self, seats: SeatsResource) -> None:
        self._seats = seats

        self.retrieve = to_streamed_response_wrapper(
            seats.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            seats.list,
        )
        self.count = to_streamed_response_wrapper(
            seats.count,
        )


class AsyncSeatsResourceWithStreamingResponse:
    def __init__(self, seats: AsyncSeatsResource) -> None:
        self._seats = seats

        self.retrieve = async_to_streamed_response_wrapper(
            seats.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            seats.list,
        )
        self.count = async_to_streamed_response_wrapper(
            seats.count,
        )
