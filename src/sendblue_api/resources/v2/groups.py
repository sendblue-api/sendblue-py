# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import group_rename_params
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

        Args:
          group_name: New group name; whitespace-only values are rejected, while null or an empty
              string clears it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            path_template("/api/v2/groups/{group_id}/name", group_id=group_id),
            body=maybe_transform({"group_name": group_name}, group_rename_params.GroupRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRenameResponse,
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

        Args:
          group_name: New group name; whitespace-only values are rejected, while null or an empty
              string clears it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            path_template("/api/v2/groups/{group_id}/name", group_id=group_id),
            body=await async_maybe_transform({"group_name": group_name}, group_rename_params.GroupRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRenameResponse,
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


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.rename = async_to_raw_response_wrapper(
            groups.rename,
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


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.rename = async_to_streamed_response_wrapper(
            groups.rename,
        )
