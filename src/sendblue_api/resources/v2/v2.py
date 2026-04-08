# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def totp(self) -> TotpResource:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return TotpResource(self._client)

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


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def totp(self) -> AsyncTotpResource:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncTotpResource(self._client)

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


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def totp(self) -> TotpResourceWithRawResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return TotpResourceWithRawResponse(self._v2.totp)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def totp(self) -> AsyncTotpResourceWithRawResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncTotpResourceWithRawResponse(self._v2.totp)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def totp(self) -> TotpResourceWithStreamingResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return TotpResourceWithStreamingResponse(self._v2.totp)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def totp(self) -> AsyncTotpResourceWithStreamingResponse:
        """Store and retrieve TOTP codes for agent 2FA (authenticator app replacement)"""
        return AsyncTotpResourceWithStreamingResponse(self._v2.totp)
