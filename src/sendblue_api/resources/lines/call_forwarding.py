# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.lines import call_forwarding_update_params
from ..._base_client import make_request_options
from ...types.lines.call_forwarding_delete_response import CallForwardingDeleteResponse
from ...types.lines.call_forwarding_update_response import CallForwardingUpdateResponse
from ...types.lines.call_forwarding_retrieve_response import CallForwardingRetrieveResponse

__all__ = ["CallForwardingResource", "AsyncCallForwardingResource"]


class CallForwardingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallForwardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return CallForwardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallForwardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return CallForwardingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        sendblue_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallForwardingRetrieveResponse:
        """
        Returns the current call forwarding number for a dedicated phone line.

        Per-line forwarding takes priority over the company default forwarding number
        but is overridden by seat-level forwarding when a seat has a forwarding number
        set.

        **Priority order:** seat forwarding → per-line forwarding → company default
        forwarding

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sendblue_number:
            raise ValueError(f"Expected a non-empty value for `sendblue_number` but received {sendblue_number!r}")
        return self._get(
            path_template("/api/lines/{sendblue_number}/call-forwarding", sendblue_number=sendblue_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallForwardingRetrieveResponse,
        )

    def update(
        self,
        sendblue_number: str,
        *,
        forwarding_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallForwardingUpdateResponse:
        """Sets a call forwarding number for a specific dedicated phone line.

        Inbound calls
        to this line will be forwarded to the specified number.

        The `forwarding_number` is normalized to E.164 format before storage. US numbers
        can be supplied in local format (e.g. `2125550199`).

        Args:
          forwarding_number: Phone number to forward calls to (E.164 or US local format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sendblue_number:
            raise ValueError(f"Expected a non-empty value for `sendblue_number` but received {sendblue_number!r}")
        return self._put(
            path_template("/api/lines/{sendblue_number}/call-forwarding", sendblue_number=sendblue_number),
            body=maybe_transform(
                {"forwarding_number": forwarding_number}, call_forwarding_update_params.CallForwardingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallForwardingUpdateResponse,
        )

    def delete(
        self,
        sendblue_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallForwardingDeleteResponse:
        """Removes the per-line call forwarding number.

        After clearing, inbound calls will
        fall back to the company default forwarding number (if configured).

        This operation is idempotent — calling it on a line with no forwarding set
        returns 200 with `forwarding_number: null`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sendblue_number:
            raise ValueError(f"Expected a non-empty value for `sendblue_number` but received {sendblue_number!r}")
        return self._delete(
            path_template("/api/lines/{sendblue_number}/call-forwarding", sendblue_number=sendblue_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallForwardingDeleteResponse,
        )


class AsyncCallForwardingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallForwardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCallForwardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallForwardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncCallForwardingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        sendblue_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallForwardingRetrieveResponse:
        """
        Returns the current call forwarding number for a dedicated phone line.

        Per-line forwarding takes priority over the company default forwarding number
        but is overridden by seat-level forwarding when a seat has a forwarding number
        set.

        **Priority order:** seat forwarding → per-line forwarding → company default
        forwarding

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sendblue_number:
            raise ValueError(f"Expected a non-empty value for `sendblue_number` but received {sendblue_number!r}")
        return await self._get(
            path_template("/api/lines/{sendblue_number}/call-forwarding", sendblue_number=sendblue_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallForwardingRetrieveResponse,
        )

    async def update(
        self,
        sendblue_number: str,
        *,
        forwarding_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallForwardingUpdateResponse:
        """Sets a call forwarding number for a specific dedicated phone line.

        Inbound calls
        to this line will be forwarded to the specified number.

        The `forwarding_number` is normalized to E.164 format before storage. US numbers
        can be supplied in local format (e.g. `2125550199`).

        Args:
          forwarding_number: Phone number to forward calls to (E.164 or US local format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sendblue_number:
            raise ValueError(f"Expected a non-empty value for `sendblue_number` but received {sendblue_number!r}")
        return await self._put(
            path_template("/api/lines/{sendblue_number}/call-forwarding", sendblue_number=sendblue_number),
            body=await async_maybe_transform(
                {"forwarding_number": forwarding_number}, call_forwarding_update_params.CallForwardingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallForwardingUpdateResponse,
        )

    async def delete(
        self,
        sendblue_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallForwardingDeleteResponse:
        """Removes the per-line call forwarding number.

        After clearing, inbound calls will
        fall back to the company default forwarding number (if configured).

        This operation is idempotent — calling it on a line with no forwarding set
        returns 200 with `forwarding_number: null`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sendblue_number:
            raise ValueError(f"Expected a non-empty value for `sendblue_number` but received {sendblue_number!r}")
        return await self._delete(
            path_template("/api/lines/{sendblue_number}/call-forwarding", sendblue_number=sendblue_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallForwardingDeleteResponse,
        )


class CallForwardingResourceWithRawResponse:
    def __init__(self, call_forwarding: CallForwardingResource) -> None:
        self._call_forwarding = call_forwarding

        self.retrieve = to_raw_response_wrapper(
            call_forwarding.retrieve,
        )
        self.update = to_raw_response_wrapper(
            call_forwarding.update,
        )
        self.delete = to_raw_response_wrapper(
            call_forwarding.delete,
        )


class AsyncCallForwardingResourceWithRawResponse:
    def __init__(self, call_forwarding: AsyncCallForwardingResource) -> None:
        self._call_forwarding = call_forwarding

        self.retrieve = async_to_raw_response_wrapper(
            call_forwarding.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            call_forwarding.update,
        )
        self.delete = async_to_raw_response_wrapper(
            call_forwarding.delete,
        )


class CallForwardingResourceWithStreamingResponse:
    def __init__(self, call_forwarding: CallForwardingResource) -> None:
        self._call_forwarding = call_forwarding

        self.retrieve = to_streamed_response_wrapper(
            call_forwarding.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            call_forwarding.update,
        )
        self.delete = to_streamed_response_wrapper(
            call_forwarding.delete,
        )


class AsyncCallForwardingResourceWithStreamingResponse:
    def __init__(self, call_forwarding: AsyncCallForwardingResource) -> None:
        self._call_forwarding = call_forwarding

        self.retrieve = async_to_streamed_response_wrapper(
            call_forwarding.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            call_forwarding.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            call_forwarding.delete,
        )
