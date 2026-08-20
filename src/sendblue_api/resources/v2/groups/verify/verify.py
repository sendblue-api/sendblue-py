# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .services.services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)

__all__ = ["VerifyResource", "AsyncVerifyResource"]


class VerifyResource(SyncAPIResource):
    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

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
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

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
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._verify.services)


class AsyncVerifyResourceWithRawResponse:
    def __init__(self, verify: AsyncVerifyResource) -> None:
        self._verify = verify

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._verify.services)


class VerifyResourceWithStreamingResponse:
    def __init__(self, verify: VerifyResource) -> None:
        self._verify = verify

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._verify.services)


class AsyncVerifyResourceWithStreamingResponse:
    def __init__(self, verify: AsyncVerifyResource) -> None:
        self._verify = verify

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._verify.services)
