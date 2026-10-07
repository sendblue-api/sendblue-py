# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import line_get_contact_status_params
from ..._types import Body, Query, Headers, NotGiven, not_given
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
from .call_forwarding import (
    CallForwardingResource,
    AsyncCallForwardingResource,
    CallForwardingResourceWithRawResponse,
    AsyncCallForwardingResourceWithRawResponse,
    CallForwardingResourceWithStreamingResponse,
    AsyncCallForwardingResourceWithStreamingResponse,
)
from ...types.line_usage_response import LineUsageResponse
from ...types.line_get_state_response import LineGetStateResponse
from ...types.line_contact_status_response import LineContactStatusResponse

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

    def get_contact_status(
        self,
        *,
        number: str,
        sendblue_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LineContactStatusResponse:
        """Check whether a contact is known or new on one of your Sendblue lines.

        The
        result uses the same message history and inactivity window as new-contact
        limits. Incoming messages and outgoing messages accepted for sending count as
        activity; rejected requests do not. A saved contact is not required, and
        activity on another line or account does not count.

        The lookup does not reserve capacity. Other sending rules still apply.
        Line-scoped temporary tokens can query only the lines they allow. Only number
        and sendblue_number query parameters are accepted.

        Args:
          number: Contact phone number (E.164 format). Formatted phone numbers are converted to
              E.164; email addresses are not supported.

          sendblue_number: Your Sendblue phone number (E.164 format). Old lines still available during a
              replacement grace period are also supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/lines/contact-status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "number": number,
                        "sendblue_number": sendblue_number,
                    },
                    line_get_contact_status_params.LineGetContactStatusParams,
                ),
            ),
            cast_to=LineContactStatusResponse,
        )

    def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LineUsageResponse:
        """
        Get each line's hourly and daily new-contact usage, limits, remaining capacity,
        and when capacity becomes available again. Includes your account's phone lines
        and old lines still available during a replacement grace period. The hourly
        window is a rolling 60 minutes; daily usage resets at 3 AM ET
        (America/New_York). Counts apply to new contacts you message, rather than
        contacts you add to your account. Dashboard messages and automations use the
        same limits.

        Requests do not reserve capacity. Recovery times assume no further sends. This
        endpoint accepts no query parameters. Use API credentials or an account-scoped
        temporary token.
        """
        return self._get(
            "/api/v2/lines/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LineUsageResponse,
        )

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

    async def get_contact_status(
        self,
        *,
        number: str,
        sendblue_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LineContactStatusResponse:
        """Check whether a contact is known or new on one of your Sendblue lines.

        The
        result uses the same message history and inactivity window as new-contact
        limits. Incoming messages and outgoing messages accepted for sending count as
        activity; rejected requests do not. A saved contact is not required, and
        activity on another line or account does not count.

        The lookup does not reserve capacity. Other sending rules still apply.
        Line-scoped temporary tokens can query only the lines they allow. Only number
        and sendblue_number query parameters are accepted.

        Args:
          number: Contact phone number (E.164 format). Formatted phone numbers are converted to
              E.164; email addresses are not supported.

          sendblue_number: Your Sendblue phone number (E.164 format). Old lines still available during a
              replacement grace period are also supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/lines/contact-status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "number": number,
                        "sendblue_number": sendblue_number,
                    },
                    line_get_contact_status_params.LineGetContactStatusParams,
                ),
            ),
            cast_to=LineContactStatusResponse,
        )

    async def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LineUsageResponse:
        """
        Get each line's hourly and daily new-contact usage, limits, remaining capacity,
        and when capacity becomes available again. Includes your account's phone lines
        and old lines still available during a replacement grace period. The hourly
        window is a rolling 60 minutes; daily usage resets at 3 AM ET
        (America/New_York). Counts apply to new contacts you message, rather than
        contacts you add to your account. Dashboard messages and automations use the
        same limits.

        Requests do not reserve capacity. Recovery times assume no further sends. This
        endpoint accepts no query parameters. Use API credentials or an account-scoped
        temporary token.
        """
        return await self._get(
            "/api/v2/lines/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LineUsageResponse,
        )

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

        self.get_contact_status = to_raw_response_wrapper(
            lines.get_contact_status,
        )
        self.get_usage = to_raw_response_wrapper(
            lines.get_usage,
        )
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

        self.get_contact_status = async_to_raw_response_wrapper(
            lines.get_contact_status,
        )
        self.get_usage = async_to_raw_response_wrapper(
            lines.get_usage,
        )
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

        self.get_contact_status = to_streamed_response_wrapper(
            lines.get_contact_status,
        )
        self.get_usage = to_streamed_response_wrapper(
            lines.get_usage,
        )
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

        self.get_contact_status = async_to_streamed_response_wrapper(
            lines.get_contact_status,
        )
        self.get_usage = async_to_streamed_response_wrapper(
            lines.get_usage,
        )
        self.get_state = async_to_streamed_response_wrapper(
            lines.get_state,
        )

    @cached_property
    def call_forwarding(self) -> AsyncCallForwardingResourceWithStreamingResponse:
        """Sendblue line configuration and health state"""
        return AsyncCallForwardingResourceWithStreamingResponse(self._lines.call_forwarding)
