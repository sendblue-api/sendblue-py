# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import verified_contact_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.verified_contact_list_response import VerifiedContactListResponse
from ..types.verified_contact_create_response import VerifiedContactCreateResponse
from ..types.verified_contact_retrieve_response import VerifiedContactRetrieveResponse

__all__ = ["VerifiedContactsResource", "AsyncVerifiedContactsResource"]


class VerifiedContactsResource(SyncAPIResource):
    """Operations for managing verified contacts on shared iMessage lines"""

    @cached_property
    def with_raw_response(self) -> VerifiedContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return VerifiedContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiedContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return VerifiedContactsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifiedContactCreateResponse:
        """
        Creates or returns a pending verified-contact route for the authenticated
        account's shared iMessage line. The recipient must send any iMessage or SMS to
        the returned line phone number to complete verification.

        Args:
          phone_number: Contact phone number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/verified-contacts",
            body=maybe_transform(
                {"phone_number": phone_number}, verified_contact_create_params.VerifiedContactCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedContactCreateResponse,
        )

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifiedContactRetrieveResponse:
        """
        Retrieve one verified-contact route by phone number for the authenticated
        account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template("/v3/verified-contacts/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedContactRetrieveResponse,
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
    ) -> VerifiedContactListResponse:
        """
        Lists the contacts attached to the authenticated account's shared iMessage line.
        Contacts start as `pending`; they become `verified` after the recipient sends an
        inbound iMessage or SMS to the shared line.
        """
        return self._get(
            "/v3/verified-contacts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedContactListResponse,
        )


class AsyncVerifiedContactsResource(AsyncAPIResource):
    """Operations for managing verified contacts on shared iMessage lines"""

    @cached_property
    def with_raw_response(self) -> AsyncVerifiedContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifiedContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiedContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncVerifiedContactsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifiedContactCreateResponse:
        """
        Creates or returns a pending verified-contact route for the authenticated
        account's shared iMessage line. The recipient must send any iMessage or SMS to
        the returned line phone number to complete verification.

        Args:
          phone_number: Contact phone number in E.164 format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/verified-contacts",
            body=await async_maybe_transform(
                {"phone_number": phone_number}, verified_contact_create_params.VerifiedContactCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedContactCreateResponse,
        )

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifiedContactRetrieveResponse:
        """
        Retrieve one verified-contact route by phone number for the authenticated
        account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template("/v3/verified-contacts/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedContactRetrieveResponse,
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
    ) -> VerifiedContactListResponse:
        """
        Lists the contacts attached to the authenticated account's shared iMessage line.
        Contacts start as `pending`; they become `verified` after the recipient sends an
        inbound iMessage or SMS to the shared line.
        """
        return await self._get(
            "/v3/verified-contacts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedContactListResponse,
        )


class VerifiedContactsResourceWithRawResponse:
    def __init__(self, verified_contacts: VerifiedContactsResource) -> None:
        self._verified_contacts = verified_contacts

        self.create = to_raw_response_wrapper(
            verified_contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            verified_contacts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            verified_contacts.list,
        )


class AsyncVerifiedContactsResourceWithRawResponse:
    def __init__(self, verified_contacts: AsyncVerifiedContactsResource) -> None:
        self._verified_contacts = verified_contacts

        self.create = async_to_raw_response_wrapper(
            verified_contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            verified_contacts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            verified_contacts.list,
        )


class VerifiedContactsResourceWithStreamingResponse:
    def __init__(self, verified_contacts: VerifiedContactsResource) -> None:
        self._verified_contacts = verified_contacts

        self.create = to_streamed_response_wrapper(
            verified_contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            verified_contacts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            verified_contacts.list,
        )


class AsyncVerifiedContactsResourceWithStreamingResponse:
    def __init__(self, verified_contacts: AsyncVerifiedContactsResource) -> None:
        self._verified_contacts = verified_contacts

        self.create = async_to_streamed_response_wrapper(
            verified_contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            verified_contacts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            verified_contacts.list,
        )
