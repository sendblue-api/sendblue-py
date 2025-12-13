# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from ...types import contact_list_params, contact_create_params, contact_update_params, contact_verify_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.contact_list_response import ContactListResponse
from ...types.contact_count_response import ContactCountResponse
from ...types.contact_create_response import ContactCreateResponse
from ...types.contact_delete_response import ContactDeleteResponse
from ...types.contact_update_response import ContactUpdateResponse
from ...types.contact_verify_response import ContactVerifyResponse
from ...types.contact_retrieve_response import ContactRetrieveResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        number: str,
        body_assigned_to_email_1: str | Omit = omit,
        body_assigned_to_email_2: str | Omit = omit,
        body_first_name_1: str | Omit = omit,
        body_first_name_2: str | Omit = omit,
        body_last_name_1: str | Omit = omit,
        body_last_name_2: str | Omit = omit,
        body_phone_number_1: str | Omit = omit,
        body_phone_number_2: str | Omit = omit,
        body_sendblue_number_1: str | Omit = omit,
        body_sendblue_number_2: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        update_if_exists: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Create a new contact or update existing if update_if_exists is true

        Args:
          number: Contact's phone number in E.164 format (preferred)

          body_assigned_to_email_1: Email of assigned user (preferred)

          body_assigned_to_email_2: Email of assigned user (deprecated, use assigned_to_email)

          body_first_name_1: Contact's first name (preferred)

          body_first_name_2: Contact's first name (deprecated, use first_name)

          body_last_name_1: Contact's last name (preferred)

          body_last_name_2: Contact's last name (deprecated, use last_name)

          body_phone_number_1: Contact's phone number (deprecated, use number)

          body_phone_number_2: Contact's phone number (deprecated, use number)

          body_sendblue_number_1: Associated Sendblue phone number to send with (preferred)

          body_sendblue_number_2: Associated Sendblue phone number (deprecated, use sendblue_number)

          tags: Tags for the contact

          update_if_exists: If true, updates the contact if it already exists

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/contacts",
            body=maybe_transform(
                {
                    "number": number,
                    "body_assigned_to_email_1": body_assigned_to_email_1,
                    "body_assigned_to_email_2": body_assigned_to_email_2,
                    "body_first_name_1": body_first_name_1,
                    "body_first_name_2": body_first_name_2,
                    "body_last_name_1": body_last_name_1,
                    "body_last_name_2": body_last_name_2,
                    "body_phone_number_1": body_phone_number_1,
                    "body_phone_number_2": body_phone_number_2,
                    "body_sendblue_number_1": body_sendblue_number_1,
                    "body_sendblue_number_2": body_sendblue_number_2,
                    "tags": tags,
                    "update_if_exists": update_if_exists,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
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
    ) -> ContactRetrieveResponse:
        """
        Retrieve a specific contact by phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/api/v2/contacts/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    def update(
        self,
        phone_number: str,
        *,
        body_assigned_to_email_1: str | Omit = omit,
        body_assigned_to_email_2: str | Omit = omit,
        body_company_name_1: str | Omit = omit,
        body_company_name_2: str | Omit = omit,
        body_first_name_1: str | Omit = omit,
        body_first_name_2: str | Omit = omit,
        body_last_name_1: str | Omit = omit,
        body_last_name_2: str | Omit = omit,
        body_sendblue_number_1: str | Omit = omit,
        body_sendblue_number_2: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateResponse:
        """
        Update an existing contact

        Args:
          body_assigned_to_email_1: Email of assigned user (preferred)

          body_assigned_to_email_2: Deprecated, use assigned_to_email

          body_company_name_1: Company name (preferred)

          body_company_name_2: Deprecated, use company_name

          body_first_name_1: Contact's first name (preferred)

          body_first_name_2: Deprecated, use first_name

          body_last_name_1: Contact's last name (preferred)

          body_last_name_2: Deprecated, use last_name

          body_sendblue_number_1: Associated Sendblue phone number (preferred)

          body_sendblue_number_2: Deprecated, use sendblue_number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._put(
            f"/api/v2/contacts/{phone_number}",
            body=maybe_transform(
                {
                    "body_assigned_to_email_1": body_assigned_to_email_1,
                    "body_assigned_to_email_2": body_assigned_to_email_2,
                    "body_company_name_1": body_company_name_1,
                    "body_company_name_2": body_company_name_2,
                    "body_first_name_1": body_first_name_1,
                    "body_first_name_2": body_first_name_2,
                    "body_last_name_1": body_last_name_1,
                    "body_last_name_2": body_last_name_2,
                    "body_sendblue_number_1": body_sendblue_number_1,
                    "body_sendblue_number_2": body_sendblue_number_2,
                    "tags": tags,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUpdateResponse,
        )

    def list(
        self,
        *,
        cid: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        Retrieve a list of contacts for the authenticated account

        Args:
          cid: Filter by contact ID

          limit: Maximum number of contacts to return

          offset: Number of contacts to skip

          order_by: Field to sort by

          order_direction: Sort direction

          phone_number: Filter by phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cid": cid,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "phone_number": phone_number,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactDeleteResponse:
        """
        Delete a specific contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._delete(
            f"/api/v2/contacts/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactDeleteResponse,
        )

    def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCountResponse:
        """Get the total number of contacts"""
        return self._get(
            "/api/v2/contacts/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCountResponse,
        )

    def verify(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactVerifyResponse:
        """
        Send a verification message to a contact

        Args:
          number: Phone number to verify

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/contacts/verify",
            body=maybe_transform({"number": number}, contact_verify_params.ContactVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactVerifyResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sendblue-api/sendblue-py#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        number: str,
        body_assigned_to_email_1: str | Omit = omit,
        body_assigned_to_email_2: str | Omit = omit,
        body_first_name_1: str | Omit = omit,
        body_first_name_2: str | Omit = omit,
        body_last_name_1: str | Omit = omit,
        body_last_name_2: str | Omit = omit,
        body_phone_number_1: str | Omit = omit,
        body_phone_number_2: str | Omit = omit,
        body_sendblue_number_1: str | Omit = omit,
        body_sendblue_number_2: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        update_if_exists: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Create a new contact or update existing if update_if_exists is true

        Args:
          number: Contact's phone number in E.164 format (preferred)

          body_assigned_to_email_1: Email of assigned user (preferred)

          body_assigned_to_email_2: Email of assigned user (deprecated, use assigned_to_email)

          body_first_name_1: Contact's first name (preferred)

          body_first_name_2: Contact's first name (deprecated, use first_name)

          body_last_name_1: Contact's last name (preferred)

          body_last_name_2: Contact's last name (deprecated, use last_name)

          body_phone_number_1: Contact's phone number (deprecated, use number)

          body_phone_number_2: Contact's phone number (deprecated, use number)

          body_sendblue_number_1: Associated Sendblue phone number to send with (preferred)

          body_sendblue_number_2: Associated Sendblue phone number (deprecated, use sendblue_number)

          tags: Tags for the contact

          update_if_exists: If true, updates the contact if it already exists

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/contacts",
            body=await async_maybe_transform(
                {
                    "number": number,
                    "body_assigned_to_email_1": body_assigned_to_email_1,
                    "body_assigned_to_email_2": body_assigned_to_email_2,
                    "body_first_name_1": body_first_name_1,
                    "body_first_name_2": body_first_name_2,
                    "body_last_name_1": body_last_name_1,
                    "body_last_name_2": body_last_name_2,
                    "body_phone_number_1": body_phone_number_1,
                    "body_phone_number_2": body_phone_number_2,
                    "body_sendblue_number_1": body_sendblue_number_1,
                    "body_sendblue_number_2": body_sendblue_number_2,
                    "tags": tags,
                    "update_if_exists": update_if_exists,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
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
    ) -> ContactRetrieveResponse:
        """
        Retrieve a specific contact by phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/api/v2/contacts/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    async def update(
        self,
        phone_number: str,
        *,
        body_assigned_to_email_1: str | Omit = omit,
        body_assigned_to_email_2: str | Omit = omit,
        body_company_name_1: str | Omit = omit,
        body_company_name_2: str | Omit = omit,
        body_first_name_1: str | Omit = omit,
        body_first_name_2: str | Omit = omit,
        body_last_name_1: str | Omit = omit,
        body_last_name_2: str | Omit = omit,
        body_sendblue_number_1: str | Omit = omit,
        body_sendblue_number_2: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateResponse:
        """
        Update an existing contact

        Args:
          body_assigned_to_email_1: Email of assigned user (preferred)

          body_assigned_to_email_2: Deprecated, use assigned_to_email

          body_company_name_1: Company name (preferred)

          body_company_name_2: Deprecated, use company_name

          body_first_name_1: Contact's first name (preferred)

          body_first_name_2: Deprecated, use first_name

          body_last_name_1: Contact's last name (preferred)

          body_last_name_2: Deprecated, use last_name

          body_sendblue_number_1: Associated Sendblue phone number (preferred)

          body_sendblue_number_2: Deprecated, use sendblue_number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._put(
            f"/api/v2/contacts/{phone_number}",
            body=await async_maybe_transform(
                {
                    "body_assigned_to_email_1": body_assigned_to_email_1,
                    "body_assigned_to_email_2": body_assigned_to_email_2,
                    "body_company_name_1": body_company_name_1,
                    "body_company_name_2": body_company_name_2,
                    "body_first_name_1": body_first_name_1,
                    "body_first_name_2": body_first_name_2,
                    "body_last_name_1": body_last_name_1,
                    "body_last_name_2": body_last_name_2,
                    "body_sendblue_number_1": body_sendblue_number_1,
                    "body_sendblue_number_2": body_sendblue_number_2,
                    "tags": tags,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUpdateResponse,
        )

    async def list(
        self,
        *,
        cid: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        order_direction: Literal["asc", "desc"] | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        Retrieve a list of contacts for the authenticated account

        Args:
          cid: Filter by contact ID

          limit: Maximum number of contacts to return

          offset: Number of contacts to skip

          order_by: Field to sort by

          order_direction: Sort direction

          phone_number: Filter by phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cid": cid,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "phone_number": phone_number,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    async def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactDeleteResponse:
        """
        Delete a specific contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._delete(
            f"/api/v2/contacts/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactDeleteResponse,
        )

    async def count(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCountResponse:
        """Get the total number of contacts"""
        return await self._get(
            "/api/v2/contacts/count",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCountResponse,
        )

    async def verify(
        self,
        *,
        number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactVerifyResponse:
        """
        Send a verification message to a contact

        Args:
          number: Phone number to verify

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/contacts/verify",
            body=await async_maybe_transform({"number": number}, contact_verify_params.ContactVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactVerifyResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contacts.update,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = to_raw_response_wrapper(
            contacts.delete,
        )
        self.count = to_raw_response_wrapper(
            contacts.count,
        )
        self.verify = to_raw_response_wrapper(
            contacts.verify,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._contacts.bulk)


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contacts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contacts.delete,
        )
        self.count = async_to_raw_response_wrapper(
            contacts.count,
        )
        self.verify = async_to_raw_response_wrapper(
            contacts.verify,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._contacts.bulk)


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contacts.delete,
        )
        self.count = to_streamed_response_wrapper(
            contacts.count,
        )
        self.verify = to_streamed_response_wrapper(
            contacts.verify,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._contacts.bulk)


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contacts.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            contacts.count,
        )
        self.verify = async_to_streamed_response_wrapper(
            contacts.verify,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._contacts.bulk)
