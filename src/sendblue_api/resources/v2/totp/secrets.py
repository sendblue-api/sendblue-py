# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.totp import secret_create_params
from ....types.v2.totp.secret_list_response import SecretListResponse
from ....types.v2.totp.secret_create_response import SecretCreateResponse
from ....types.v2.totp.secret_delete_response import SecretDeleteResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""

    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        algorithm: Literal["SHA1", "SHA256", "SHA512"] | Omit = omit,
        digits: Literal[6, 8] | Omit = omit,
        issuer: str | Omit = omit,
        label: str | Omit = omit,
        period: int | Omit = omit,
        secret: str | Omit = omit,
        uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretCreateResponse:
        """Store an encrypted TOTP secret for your account.

        Agents can use this instead of
        a phone-based authenticator app.

        Provide either:

        - A `uri` (the `otpauth://` URI from a QR code scan), which auto-populates all
          fields
        - A base32 `secret` with optional `label`, `issuer`, `algorithm`, `digits`, and
          `period`

        Args:
          algorithm: Hash algorithm

          digits: Code length

          issuer: Service name (e.g. "GitHub", "Google")

          label: Human-readable label for this secret (e.g. "GitHub - agent@example.com").
              Required unless `uri` is provided.

          period: Rotation period in seconds

          secret: Base32-encoded TOTP secret. Omit to auto-generate one.

          uri: Full `otpauth://totp/...` URI from a QR code. Overrides all other fields if
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/totp/secrets",
            body=maybe_transform(
                {
                    "algorithm": algorithm,
                    "digits": digits,
                    "issuer": issuer,
                    "label": label,
                    "period": period,
                    "secret": secret,
                    "uri": uri,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """List all stored TOTP secrets for the account.

        The encrypted secret values are
        never returned.
        """
        return self._get(
            "/api/v2/totp/secrets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretListResponse,
        )

    def delete(
        self,
        secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretDeleteResponse:
        """
        Permanently delete a stored TOTP secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._delete(
            path_template("/api/v2/totp/secrets/{secret_id}", secret_id=secret_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretDeleteResponse,
        )


class AsyncSecretsResource(AsyncAPIResource):
    """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""

    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        algorithm: Literal["SHA1", "SHA256", "SHA512"] | Omit = omit,
        digits: Literal[6, 8] | Omit = omit,
        issuer: str | Omit = omit,
        label: str | Omit = omit,
        period: int | Omit = omit,
        secret: str | Omit = omit,
        uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretCreateResponse:
        """Store an encrypted TOTP secret for your account.

        Agents can use this instead of
        a phone-based authenticator app.

        Provide either:

        - A `uri` (the `otpauth://` URI from a QR code scan), which auto-populates all
          fields
        - A base32 `secret` with optional `label`, `issuer`, `algorithm`, `digits`, and
          `period`

        Args:
          algorithm: Hash algorithm

          digits: Code length

          issuer: Service name (e.g. "GitHub", "Google")

          label: Human-readable label for this secret (e.g. "GitHub - agent@example.com").
              Required unless `uri` is provided.

          period: Rotation period in seconds

          secret: Base32-encoded TOTP secret. Omit to auto-generate one.

          uri: Full `otpauth://totp/...` URI from a QR code. Overrides all other fields if
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/totp/secrets",
            body=await async_maybe_transform(
                {
                    "algorithm": algorithm,
                    "digits": digits,
                    "issuer": issuer,
                    "label": label,
                    "period": period,
                    "secret": secret,
                    "uri": uri,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretListResponse:
        """List all stored TOTP secrets for the account.

        The encrypted secret values are
        never returned.
        """
        return await self._get(
            "/api/v2/totp/secrets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretListResponse,
        )

    async def delete(
        self,
        secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecretDeleteResponse:
        """
        Permanently delete a stored TOTP secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._delete(
            path_template("/api/v2/totp/secrets/{secret_id}", secret_id=secret_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretDeleteResponse,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
