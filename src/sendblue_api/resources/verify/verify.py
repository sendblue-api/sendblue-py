# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .verifications import (
    VerificationsResource,
    AsyncVerificationsResource,
    VerificationsResourceWithRawResponse,
    AsyncVerificationsResourceWithRawResponse,
    VerificationsResourceWithStreamingResponse,
    AsyncVerificationsResourceWithStreamingResponse,
)

__all__ = ["VerifyResource", "AsyncVerifyResource"]


class VerifyResource(SyncAPIResource):
    @cached_property
    def verifications(self) -> VerificationsResource:
        """Sendblue Verify issuance and recovery state"""
        return VerificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return VerifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return VerifyResourceWithStreamingResponse(self)


class AsyncVerifyResource(AsyncAPIResource):
    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """Sendblue Verify issuance and recovery state"""
        return AsyncVerificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncVerifyResourceWithStreamingResponse(self)


class VerifyResourceWithRawResponse:
    def __init__(self, verify: VerifyResource) -> None:
        self._verify = verify

    @cached_property
    def verifications(self) -> VerificationsResourceWithRawResponse:
        """Sendblue Verify issuance and recovery state"""
        return VerificationsResourceWithRawResponse(self._verify.verifications)


class AsyncVerifyResourceWithRawResponse:
    def __init__(self, verify: AsyncVerifyResource) -> None:
        self._verify = verify

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithRawResponse:
        """Sendblue Verify issuance and recovery state"""
        return AsyncVerificationsResourceWithRawResponse(self._verify.verifications)


class VerifyResourceWithStreamingResponse:
    def __init__(self, verify: VerifyResource) -> None:
        self._verify = verify

    @cached_property
    def verifications(self) -> VerificationsResourceWithStreamingResponse:
        """Sendblue Verify issuance and recovery state"""
        return VerificationsResourceWithStreamingResponse(self._verify.verifications)


class AsyncVerifyResourceWithStreamingResponse:
    def __init__(self, verify: AsyncVerifyResource) -> None:
        self._verify = verify

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """Sendblue Verify issuance and recovery state"""
        return AsyncVerificationsResourceWithStreamingResponse(self._verify.verifications)
