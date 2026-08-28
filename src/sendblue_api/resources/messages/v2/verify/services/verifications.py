# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.messages.v2.verify.services import verification_create_params
from ......types.messages.v2.verify.services.verification_create_response import VerificationCreateResponse
from ......types.messages.v2.verify.services.verification_retrieve_response import VerificationRetrieveResponse

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

    def create(
        self,
        service_sid: str,
        *,
        to: str,
        hosted: verification_create_params.Hosted | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """Creates an inverted-OTP verification for the supplied E.164 phone number.

        The
        user must send the returned code from that exact phone number to the returned
        Sendblue destination number.

        Include `hosted` to create an origin-bound Hosted Verify widget session.
        Sendblue API credentials must remain on the customer's backend; only the
        returned `hosted` values may be sent to the browser. Twilio-compatible clients
        may alternatively send the API Key ID and API Secret Key with HTTP Basic
        authentication. Temporary bearer authentication is supported for account-scoped
        tokens; line-scoped temporary tokens cannot create account-wide Verifications.

        Args:
          to: E.164 phone number that must send the verification message.

          hosted: Options for an origin-bound Hosted Verify widget session. Nested keys are strict
              snake_case. `parent_origin` must be an exact HTTPS origin with a DNS hostname.
              `127.0.0.1` is also accepted, and HTTP is allowed only for `localhost` or
              `127.0.0.1` development origins. Wildcards and other IP literals are rejected
              because browsers cannot enforce them as exact CSP `frame-ancestors` sources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_sid:
            raise ValueError(f"Expected a non-empty value for `service_sid` but received {service_sid!r}")
        return self._post(
            path_template("/api/v2/verify/services/{service_sid}/verifications", service_sid=service_sid),
            body=maybe_transform(
                {
                    "to": to,
                    "hosted": hosted,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    def retrieve(
        self,
        verification_sid: str,
        *,
        service_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationRetrieveResponse:
        """
        Returns the authoritative status for one Verification owned by the authenticated
        account. Twilio-compatible clients may send the API Key ID and API Secret Key
        with HTTP Basic authentication. Temporary bearer authentication is supported for
        account-scoped tokens; line-scoped temporary tokens cannot retrieve account-wide
        Verification state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_sid:
            raise ValueError(f"Expected a non-empty value for `service_sid` but received {service_sid!r}")
        if not verification_sid:
            raise ValueError(f"Expected a non-empty value for `verification_sid` but received {verification_sid!r}")
        return self._get(
            path_template(
                "/api/v2/verify/services/{service_sid}/verifications/{verification_sid}",
                service_sid=service_sid,
                verification_sid=verification_sid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
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

    async def create(
        self,
        service_sid: str,
        *,
        to: str,
        hosted: verification_create_params.Hosted | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """Creates an inverted-OTP verification for the supplied E.164 phone number.

        The
        user must send the returned code from that exact phone number to the returned
        Sendblue destination number.

        Include `hosted` to create an origin-bound Hosted Verify widget session.
        Sendblue API credentials must remain on the customer's backend; only the
        returned `hosted` values may be sent to the browser. Twilio-compatible clients
        may alternatively send the API Key ID and API Secret Key with HTTP Basic
        authentication. Temporary bearer authentication is supported for account-scoped
        tokens; line-scoped temporary tokens cannot create account-wide Verifications.

        Args:
          to: E.164 phone number that must send the verification message.

          hosted: Options for an origin-bound Hosted Verify widget session. Nested keys are strict
              snake_case. `parent_origin` must be an exact HTTPS origin with a DNS hostname.
              `127.0.0.1` is also accepted, and HTTP is allowed only for `localhost` or
              `127.0.0.1` development origins. Wildcards and other IP literals are rejected
              because browsers cannot enforce them as exact CSP `frame-ancestors` sources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_sid:
            raise ValueError(f"Expected a non-empty value for `service_sid` but received {service_sid!r}")
        return await self._post(
            path_template("/api/v2/verify/services/{service_sid}/verifications", service_sid=service_sid),
            body=await async_maybe_transform(
                {
                    "to": to,
                    "hosted": hosted,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    async def retrieve(
        self,
        verification_sid: str,
        *,
        service_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationRetrieveResponse:
        """
        Returns the authoritative status for one Verification owned by the authenticated
        account. Twilio-compatible clients may send the API Key ID and API Secret Key
        with HTTP Basic authentication. Temporary bearer authentication is supported for
        account-scoped tokens; line-scoped temporary tokens cannot retrieve account-wide
        Verification state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service_sid:
            raise ValueError(f"Expected a non-empty value for `service_sid` but received {service_sid!r}")
        if not verification_sid:
            raise ValueError(f"Expected a non-empty value for `verification_sid` but received {verification_sid!r}")
        return await self._get(
            path_template(
                "/api/v2/verify/services/{service_sid}/verifications/{verification_sid}",
                service_sid=service_sid,
                verification_sid=verification_sid,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
        )


class VerificationsResourceWithRawResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.create = to_raw_response_wrapper(
            verifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            verifications.retrieve,
        )


class AsyncVerificationsResourceWithRawResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.create = async_to_raw_response_wrapper(
            verifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            verifications.retrieve,
        )


class VerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.create = to_streamed_response_wrapper(
            verifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            verifications.retrieve,
        )


class AsyncVerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.create = async_to_streamed_response_wrapper(
            verifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            verifications.retrieve,
        )
