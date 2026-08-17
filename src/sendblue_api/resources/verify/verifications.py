# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.verify import verification_list_params
from ...types.verify.verification_list_response import VerificationListResponse

__all__ = ["VerificationsResource", "AsyncVerificationsResource"]


class VerificationsResource(SyncAPIResource):
    """Sendblue Verify issuance and recovery state"""

    @cached_property
    def with_raw_response(self) -> VerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return VerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return VerificationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationListResponse:
        """
        Account-scoped verification state used to recover terminal Verify events after
        an SSE gap.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/verify/verifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "updated_at_gte": updated_at_gte,
                    },
                    verification_list_params.VerificationListParams,
                ),
            ),
            cast_to=VerificationListResponse,
        )


class AsyncVerificationsResource(AsyncAPIResource):
    """Sendblue Verify issuance and recovery state"""

    @cached_property
    def with_raw_response(self) -> AsyncVerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncVerificationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationListResponse:
        """
        Account-scoped verification state used to recover terminal Verify events after
        an SSE gap.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/verify/verifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "updated_at_gte": updated_at_gte,
                    },
                    verification_list_params.VerificationListParams,
                ),
            ),
            cast_to=VerificationListResponse,
        )


class VerificationsResourceWithRawResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.list = to_raw_response_wrapper(
            verifications.list,
        )


class AsyncVerificationsResourceWithRawResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.list = async_to_raw_response_wrapper(
            verifications.list,
        )


class VerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.list = to_streamed_response_wrapper(
            verifications.list,
        )


class AsyncVerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.list = async_to_streamed_response_wrapper(
            verifications.list,
        )
