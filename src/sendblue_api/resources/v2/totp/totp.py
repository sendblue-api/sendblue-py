# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.totp_get_code_response import TotpGetCodeResponse

__all__ = ["TotpResource", "AsyncTotpResource"]


class TotpResource(SyncAPIResource):
    """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""

    @cached_property
    def secrets(self) -> SecretsResource:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TotpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return TotpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return TotpResourceWithStreamingResponse(self)

    def get_code(
        self,
        secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TotpGetCodeResponse:
        """
        Generate the current 6- or 8-digit TOTP code for a stored secret, along with how
        many seconds remain until it rotates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._get(
            path_template("/api/v2/totp/code/{secret_id}", secret_id=secret_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TotpGetCodeResponse,
        )


class AsyncTotpResource(AsyncAPIResource):
    """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTotpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTotpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncTotpResourceWithStreamingResponse(self)

    async def get_code(
        self,
        secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TotpGetCodeResponse:
        """
        Generate the current 6- or 8-digit TOTP code for a stored secret, along with how
        many seconds remain until it rotates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._get(
            path_template("/api/v2/totp/code/{secret_id}", secret_id=secret_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TotpGetCodeResponse,
        )


class TotpResourceWithRawResponse:
    def __init__(self, totp: TotpResource) -> None:
        self._totp = totp

        self.get_code = to_raw_response_wrapper(
            totp.get_code,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return SecretsResourceWithRawResponse(self._totp.secrets)


class AsyncTotpResourceWithRawResponse:
    def __init__(self, totp: AsyncTotpResource) -> None:
        self._totp = totp

        self.get_code = async_to_raw_response_wrapper(
            totp.get_code,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncSecretsResourceWithRawResponse(self._totp.secrets)


class TotpResourceWithStreamingResponse:
    def __init__(self, totp: TotpResource) -> None:
        self._totp = totp

        self.get_code = to_streamed_response_wrapper(
            totp.get_code,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return SecretsResourceWithStreamingResponse(self._totp.secrets)


class AsyncTotpResourceWithStreamingResponse:
    def __init__(self, totp: AsyncTotpResource) -> None:
        self._totp = totp

        self.get_code = async_to_streamed_response_wrapper(
            totp.get_code,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncSecretsResourceWithStreamingResponse(self._totp.secrets)
