# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ......_compat import cached_property
from .verifications import (
    VerificationsResource,
    AsyncVerificationsResource,
    VerificationsResourceWithRawResponse,
    AsyncVerificationsResourceWithRawResponse,
    VerificationsResourceWithStreamingResponse,
    AsyncVerificationsResourceWithStreamingResponse,
)
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def verifications(self) -> VerificationsResource:
        """Sendblue Verify issuance and recovery state"""
        return VerificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """Sendblue Verify issuance and recovery state"""
        return AsyncVerificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

    @cached_property
    def verifications(self) -> VerificationsResourceWithRawResponse:
        """Sendblue Verify issuance and recovery state"""
        return VerificationsResourceWithRawResponse(self._services.verifications)


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithRawResponse:
        """Sendblue Verify issuance and recovery state"""
        return AsyncVerificationsResourceWithRawResponse(self._services.verifications)


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

    @cached_property
    def verifications(self) -> VerificationsResourceWithStreamingResponse:
        """Sendblue Verify issuance and recovery state"""
        return VerificationsResourceWithStreamingResponse(self._services.verifications)


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """Sendblue Verify issuance and recovery state"""
        return AsyncVerificationsResourceWithStreamingResponse(self._services.verifications)
