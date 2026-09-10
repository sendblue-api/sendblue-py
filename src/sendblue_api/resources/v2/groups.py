# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import group_rename_params, group_set_photo_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.group_rename_response import GroupRenameResponse
from ...types.v2.group_retrieve_response import GroupRetrieveResponse
from ...types.v2.group_set_photo_response import GroupSetPhotoResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    """Operations for group messaging (beta)"""

    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupRetrieveResponse:
        """
        Retrieve the current complete membership for a group owned by the authenticated
        account.

        Args:
          group_id: Modern sb*group*_ identifiers and legacy __group_id_\\** identifiers are
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template("/api/v2/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRetrieveResponse,
        )

    def rename(
        self,
        group_id: str,
        *,
        group_name: Optional[str],
        from_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupRenameResponse:
        """
        Changes the Apple-visible name of an existing iMessage group and waits for the
        Sendblue line to verify the resulting state. Pass `null` or an empty string to
        clear the name. The verified value is persisted as the group's `group_name`.

        The group must already have an iMessage chat, and the Sendblue line serving it
        must be online and support group name changes. Failed requests are not replayed
        automatically; retrying the same desired state is safe.

        By default an eligible Sendblue line in the group is selected automatically.
        Pass `from_number` to require a specific Sendblue line: it must have an iMessage
        mapping for this group, and if that line cannot act the request fails without
        falling back to another line. The success response reports the line that
        performed the change as `from_number`.

        Args:
          group_name: New group name; whitespace-only values are rejected, while null or an empty
              string clears it

          from_number: Sendblue line that must perform the change; it must have an iMessage mapping for
              this group, and no other line is used if it cannot act. Omit or pass null for
              automatic selection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            path_template("/api/v2/groups/{group_id}/name", group_id=group_id),
            body=maybe_transform(
                {
                    "group_name": group_name,
                    "from_number": from_number,
                },
                group_rename_params.GroupRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRenameResponse,
        )

    def set_photo(
        self,
        group_id: str,
        *,
        photo_url: Optional[str],
        from_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupSetPhotoResponse:
        """
        Sets the Apple-visible photo of an existing iMessage group and waits for the
        Sendblue line to verify the resulting device state. Pass `null` to clear the
        photo. A set is verified only when the device-created photo transfer becomes the
        chat's current photo; the verified photo is then persisted with the group and
        returned on group retrieval with an image URL.

        Set the photo with either a JSON `photo_url` or raw image bytes in the `file`
        field of a multipart form. Images must be JPEG, PNG, or GIF, at most 5 MB, and
        no more than 25 million aggregate decoded pixels. URL images must use a direct,
        publicly resolvable https URL; redirects are not followed. Replacing or clearing
        the photo replaces the current stored reference and attempts to delete the
        superseded object; no history is exposed through the API. Supported line types
        are checked automatically; ineligible lines return `unsupported_line`. Failed
        requests are not replayed automatically; retrying the same desired state is
        safe.

        By default an eligible Sendblue line in the group is selected automatically.
        Pass `from_number` to require a specific Sendblue line: it must have an iMessage
        mapping for this group, and if that line cannot act the request fails without
        falling back to another line. The success response reports the line that
        performed the change as `from_number`.

        Args:
          photo_url: Direct, publicly resolvable https URL of the image to set (JPEG, PNG, or GIF, at
              most 5 MB and 25 million aggregate decoded pixels; redirects are not followed);
              null clears the group photo

          from_number: Sendblue line that must perform the change; it must have an iMessage mapping for
              this group, and no other line is used if it cannot act. Omit or pass null for
              automatic selection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        body = deepcopy_with_paths(
            {
                "photo_url": photo_url,
                "from_number": from_number,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/api/v2/groups/{group_id}/photo", group_id=group_id),
            body=maybe_transform(body, group_set_photo_params.GroupSetPhotoParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupSetPhotoResponse,
        )


class AsyncGroupsResource(AsyncAPIResource):
    """Operations for group messaging (beta)"""

    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupRetrieveResponse:
        """
        Retrieve the current complete membership for a group owned by the authenticated
        account.

        Args:
          group_id: Modern sb*group*_ identifiers and legacy __group_id_\\** identifiers are
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template("/api/v2/groups/{group_id}", group_id=group_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRetrieveResponse,
        )

    async def rename(
        self,
        group_id: str,
        *,
        group_name: Optional[str],
        from_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupRenameResponse:
        """
        Changes the Apple-visible name of an existing iMessage group and waits for the
        Sendblue line to verify the resulting state. Pass `null` or an empty string to
        clear the name. The verified value is persisted as the group's `group_name`.

        The group must already have an iMessage chat, and the Sendblue line serving it
        must be online and support group name changes. Failed requests are not replayed
        automatically; retrying the same desired state is safe.

        By default an eligible Sendblue line in the group is selected automatically.
        Pass `from_number` to require a specific Sendblue line: it must have an iMessage
        mapping for this group, and if that line cannot act the request fails without
        falling back to another line. The success response reports the line that
        performed the change as `from_number`.

        Args:
          group_name: New group name; whitespace-only values are rejected, while null or an empty
              string clears it

          from_number: Sendblue line that must perform the change; it must have an iMessage mapping for
              this group, and no other line is used if it cannot act. Omit or pass null for
              automatic selection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            path_template("/api/v2/groups/{group_id}/name", group_id=group_id),
            body=await async_maybe_transform(
                {
                    "group_name": group_name,
                    "from_number": from_number,
                },
                group_rename_params.GroupRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRenameResponse,
        )

    async def set_photo(
        self,
        group_id: str,
        *,
        photo_url: Optional[str],
        from_number: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupSetPhotoResponse:
        """
        Sets the Apple-visible photo of an existing iMessage group and waits for the
        Sendblue line to verify the resulting device state. Pass `null` to clear the
        photo. A set is verified only when the device-created photo transfer becomes the
        chat's current photo; the verified photo is then persisted with the group and
        returned on group retrieval with an image URL.

        Set the photo with either a JSON `photo_url` or raw image bytes in the `file`
        field of a multipart form. Images must be JPEG, PNG, or GIF, at most 5 MB, and
        no more than 25 million aggregate decoded pixels. URL images must use a direct,
        publicly resolvable https URL; redirects are not followed. Replacing or clearing
        the photo replaces the current stored reference and attempts to delete the
        superseded object; no history is exposed through the API. Supported line types
        are checked automatically; ineligible lines return `unsupported_line`. Failed
        requests are not replayed automatically; retrying the same desired state is
        safe.

        By default an eligible Sendblue line in the group is selected automatically.
        Pass `from_number` to require a specific Sendblue line: it must have an iMessage
        mapping for this group, and if that line cannot act the request fails without
        falling back to another line. The success response reports the line that
        performed the change as `from_number`.

        Args:
          photo_url: Direct, publicly resolvable https URL of the image to set (JPEG, PNG, or GIF, at
              most 5 MB and 25 million aggregate decoded pixels; redirects are not followed);
              null clears the group photo

          from_number: Sendblue line that must perform the change; it must have an iMessage mapping for
              this group, and no other line is used if it cannot act. Omit or pass null for
              automatic selection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        body = deepcopy_with_paths(
            {
                "photo_url": photo_url,
                "from_number": from_number,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/api/v2/groups/{group_id}/photo", group_id=group_id),
            body=await async_maybe_transform(body, group_set_photo_params.GroupSetPhotoParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupSetPhotoResponse,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.retrieve = to_raw_response_wrapper(
            groups.retrieve,
        )
        self.rename = to_raw_response_wrapper(
            groups.rename,
        )
        self.set_photo = to_raw_response_wrapper(
            groups.set_photo,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.rename = async_to_raw_response_wrapper(
            groups.rename,
        )
        self.set_photo = async_to_raw_response_wrapper(
            groups.set_photo,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.retrieve = to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.rename = to_streamed_response_wrapper(
            groups.rename,
        )
        self.set_photo = to_streamed_response_wrapper(
            groups.set_photo,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.rename = async_to_streamed_response_wrapper(
            groups.rename,
        )
        self.set_photo = async_to_streamed_response_wrapper(
            groups.set_photo,
        )
