# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import groups, lookups, messages, webhooks, media_objects, typing_indicators
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, SendblueAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.contacts import contacts

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "SendblueAPI",
    "AsyncSendblueAPI",
    "Client",
    "AsyncClient",
]


class SendblueAPI(SyncAPIClient):
    messages: messages.MessagesResource
    groups: groups.GroupsResource
    media_objects: media_objects.MediaObjectsResource
    lookups: lookups.LookupsResource
    typing_indicators: typing_indicators.TypingIndicatorsResource
    contacts: contacts.ContactsResource
    webhooks: webhooks.WebhooksResource
    with_raw_response: SendblueAPIWithRawResponse
    with_streaming_response: SendblueAPIWithStreamedResponse

    # client options
    api_key: str
    api_secret: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SendblueAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SENDBLUE_API_API_KEY`
        - `api_secret` from `SENDBLUE_API_API_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("SENDBLUE_API_API_KEY")
        if api_key is None:
            raise SendblueAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENDBLUE_API_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_secret is None:
            api_secret = os.environ.get("SENDBLUE_API_API_SECRET")
        if api_secret is None:
            raise SendblueAPIError(
                "The api_secret client option must be set either by passing api_secret to the client or by setting the SENDBLUE_API_API_SECRET environment variable"
            )
        self.api_secret = api_secret

        if base_url is None:
            base_url = os.environ.get("SENDBLUE_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sendblue.co"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.messages = messages.MessagesResource(self)
        self.groups = groups.GroupsResource(self)
        self.media_objects = media_objects.MediaObjectsResource(self)
        self.lookups = lookups.LookupsResource(self)
        self.typing_indicators = typing_indicators.TypingIndicatorsResource(self)
        self.contacts = contacts.ContactsResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.with_raw_response = SendblueAPIWithRawResponse(self)
        self.with_streaming_response = SendblueAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._api_secret_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"sb-api-key-id": api_key}

    @property
    def _api_secret_auth(self) -> dict[str, str]:
        api_secret = self.api_secret
        return {"sb-api-secret-key": api_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            api_secret=api_secret or self.api_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSendblueAPI(AsyncAPIClient):
    messages: messages.AsyncMessagesResource
    groups: groups.AsyncGroupsResource
    media_objects: media_objects.AsyncMediaObjectsResource
    lookups: lookups.AsyncLookupsResource
    typing_indicators: typing_indicators.AsyncTypingIndicatorsResource
    contacts: contacts.AsyncContactsResource
    webhooks: webhooks.AsyncWebhooksResource
    with_raw_response: AsyncSendblueAPIWithRawResponse
    with_streaming_response: AsyncSendblueAPIWithStreamedResponse

    # client options
    api_key: str
    api_secret: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSendblueAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SENDBLUE_API_API_KEY`
        - `api_secret` from `SENDBLUE_API_API_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("SENDBLUE_API_API_KEY")
        if api_key is None:
            raise SendblueAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENDBLUE_API_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_secret is None:
            api_secret = os.environ.get("SENDBLUE_API_API_SECRET")
        if api_secret is None:
            raise SendblueAPIError(
                "The api_secret client option must be set either by passing api_secret to the client or by setting the SENDBLUE_API_API_SECRET environment variable"
            )
        self.api_secret = api_secret

        if base_url is None:
            base_url = os.environ.get("SENDBLUE_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sendblue.co"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.messages = messages.AsyncMessagesResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.media_objects = media_objects.AsyncMediaObjectsResource(self)
        self.lookups = lookups.AsyncLookupsResource(self)
        self.typing_indicators = typing_indicators.AsyncTypingIndicatorsResource(self)
        self.contacts = contacts.AsyncContactsResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.with_raw_response = AsyncSendblueAPIWithRawResponse(self)
        self.with_streaming_response = AsyncSendblueAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._api_secret_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"sb-api-key-id": api_key}

    @property
    def _api_secret_auth(self) -> dict[str, str]:
        api_secret = self.api_secret
        return {"sb-api-secret-key": api_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            api_secret=api_secret or self.api_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SendblueAPIWithRawResponse:
    def __init__(self, client: SendblueAPI) -> None:
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.media_objects = media_objects.MediaObjectsResourceWithRawResponse(client.media_objects)
        self.lookups = lookups.LookupsResourceWithRawResponse(client.lookups)
        self.typing_indicators = typing_indicators.TypingIndicatorsResourceWithRawResponse(client.typing_indicators)
        self.contacts = contacts.ContactsResourceWithRawResponse(client.contacts)
        self.webhooks = webhooks.WebhooksResourceWithRawResponse(client.webhooks)


class AsyncSendblueAPIWithRawResponse:
    def __init__(self, client: AsyncSendblueAPI) -> None:
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.media_objects = media_objects.AsyncMediaObjectsResourceWithRawResponse(client.media_objects)
        self.lookups = lookups.AsyncLookupsResourceWithRawResponse(client.lookups)
        self.typing_indicators = typing_indicators.AsyncTypingIndicatorsResourceWithRawResponse(
            client.typing_indicators
        )
        self.contacts = contacts.AsyncContactsResourceWithRawResponse(client.contacts)
        self.webhooks = webhooks.AsyncWebhooksResourceWithRawResponse(client.webhooks)


class SendblueAPIWithStreamedResponse:
    def __init__(self, client: SendblueAPI) -> None:
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.media_objects = media_objects.MediaObjectsResourceWithStreamingResponse(client.media_objects)
        self.lookups = lookups.LookupsResourceWithStreamingResponse(client.lookups)
        self.typing_indicators = typing_indicators.TypingIndicatorsResourceWithStreamingResponse(
            client.typing_indicators
        )
        self.contacts = contacts.ContactsResourceWithStreamingResponse(client.contacts)
        self.webhooks = webhooks.WebhooksResourceWithStreamingResponse(client.webhooks)


class AsyncSendblueAPIWithStreamedResponse:
    def __init__(self, client: AsyncSendblueAPI) -> None:
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.media_objects = media_objects.AsyncMediaObjectsResourceWithStreamingResponse(client.media_objects)
        self.lookups = lookups.AsyncLookupsResourceWithStreamingResponse(client.lookups)
        self.typing_indicators = typing_indicators.AsyncTypingIndicatorsResourceWithStreamingResponse(
            client.typing_indicators
        )
        self.contacts = contacts.AsyncContactsResourceWithStreamingResponse(client.contacts)
        self.webhooks = webhooks.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)


Client = SendblueAPI

AsyncClient = AsyncSendblueAPI
