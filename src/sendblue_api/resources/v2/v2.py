# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .seats import (
    SeatsResource,
    AsyncSeatsResource,
    SeatsResourceWithRawResponse,
    AsyncSeatsResourceWithRawResponse,
    SeatsResourceWithStreamingResponse,
    AsyncSeatsResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from .totp.totp import (
    TotpResource,
    AsyncTotpResource,
    TotpResourceWithRawResponse,
    AsyncTotpResourceWithRawResponse,
    TotpResourceWithStreamingResponse,
    AsyncTotpResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2_retrieve_group_membership_response import V2RetrieveGroupMembershipResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    """Operations for group messaging (beta)"""

    @cached_property
    def totp(self) -> TotpResource:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return TotpResource(self._client)

    @cached_property
    def seats(self) -> SeatsResource:
        """
        Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
        """
        return SeatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def retrieve_group_membership(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveGroupMembershipResponse:
        """
        Retrieve the current complete membership for a group owned by the authenticated
        account.

        Args:
          group_id: Modern sb*group*_ identifiers and legacy __group_id_\\** identifiers are
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template("/api/v2/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2RetrieveGroupMembershipResponse,
        )


class AsyncV2Resource(AsyncAPIResource):
    """Operations for group messaging (beta)"""

    @cached_property
    def totp(self) -> AsyncTotpResource:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncTotpResource(self._client)

    @cached_property
    def seats(self) -> AsyncSeatsResource:
        """
        Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
        """
        return AsyncSeatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def retrieve_group_membership(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveGroupMembershipResponse:
        """
        Retrieve the current complete membership for a group owned by the authenticated
        account.

        Args:
          group_id: Modern sb*group*_ identifiers and legacy __group_id_\\** identifiers are
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template("/api/v2/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2RetrieveGroupMembershipResponse,
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.retrieve_group_membership = to_raw_response_wrapper(
            v2.retrieve_group_membership,
        )

    @cached_property
    def totp(self) -> TotpResourceWithRawResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return TotpResourceWithRawResponse(self._v2.totp)

    @cached_property
    def seats(self) -> SeatsResourceWithRawResponse:
        """
        Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
        """
        return SeatsResourceWithRawResponse(self._v2.seats)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.retrieve_group_membership = async_to_raw_response_wrapper(
            v2.retrieve_group_membership,
        )

    @cached_property
    def totp(self) -> AsyncTotpResourceWithRawResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncTotpResourceWithRawResponse(self._v2.totp)

    @cached_property
    def seats(self) -> AsyncSeatsResourceWithRawResponse:
        """
        Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
        """
        return AsyncSeatsResourceWithRawResponse(self._v2.seats)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.retrieve_group_membership = to_streamed_response_wrapper(
            v2.retrieve_group_membership,
        )

    @cached_property
    def totp(self) -> TotpResourceWithStreamingResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return TotpResourceWithStreamingResponse(self._v2.totp)

    @cached_property
    def seats(self) -> SeatsResourceWithStreamingResponse:
        """
        Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
        """
        return SeatsResourceWithStreamingResponse(self._v2.seats)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.retrieve_group_membership = async_to_streamed_response_wrapper(
            v2.retrieve_group_membership,
        )

    @cached_property
    def totp(self) -> AsyncTotpResourceWithStreamingResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncTotpResourceWithStreamingResponse(self._v2.totp)

    @cached_property
    def seats(self) -> AsyncSeatsResourceWithStreamingResponse:
        """
        Operations for retrieving seats (users) on the account, used for attribution via `seat_id`
        """
        return AsyncSeatsResourceWithStreamingResponse(self._v2.seats)
