# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import media_object_upload_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.media_object_upload_response import MediaObjectUploadResponse

__all__ = ["MediaObjectsResource", "AsyncMediaObjectsResource"]


class MediaObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return MediaObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return MediaObjectsResourceWithStreamingResponse(self)

    def upload(
        self,
        *,
        media_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaObjectUploadResponse:
        """
        Upload a media file to Sendblue's CDN for use in messages

        Args:
          media_url: URL of the media file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/upload-media-object",
            body=maybe_transform({"media_url": media_url}, media_object_upload_params.MediaObjectUploadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaObjectUploadResponse,
        )


class AsyncMediaObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncMediaObjectsResourceWithStreamingResponse(self)

    async def upload(
        self,
        *,
        media_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaObjectUploadResponse:
        """
        Upload a media file to Sendblue's CDN for use in messages

        Args:
          media_url: URL of the media file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/upload-media-object",
            body=await async_maybe_transform(
                {"media_url": media_url}, media_object_upload_params.MediaObjectUploadParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaObjectUploadResponse,
        )


class MediaObjectsResourceWithRawResponse:
    def __init__(self, media_objects: MediaObjectsResource) -> None:
        self._media_objects = media_objects

        self.upload = to_raw_response_wrapper(
            media_objects.upload,
        )


class AsyncMediaObjectsResourceWithRawResponse:
    def __init__(self, media_objects: AsyncMediaObjectsResource) -> None:
        self._media_objects = media_objects

        self.upload = async_to_raw_response_wrapper(
            media_objects.upload,
        )


class MediaObjectsResourceWithStreamingResponse:
    def __init__(self, media_objects: MediaObjectsResource) -> None:
        self._media_objects = media_objects

        self.upload = to_streamed_response_wrapper(
            media_objects.upload,
        )


class AsyncMediaObjectsResourceWithStreamingResponse:
    def __init__(self, media_objects: AsyncMediaObjectsResource) -> None:
        self._media_objects = media_objects

        self.upload = async_to_streamed_response_wrapper(
            media_objects.upload,
        )
