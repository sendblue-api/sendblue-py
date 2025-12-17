# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, SendblueAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import groups, lookups, contacts, messages, webhooks, media_objects, typing_indicators
    from .resources.groups import GroupsResource, AsyncGroupsResource
    from .resources.lookups import LookupsResource, AsyncLookupsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.media_objects import MediaObjectsResource, AsyncMediaObjectsResource
    from .resources.contacts.contacts import ContactsResource, AsyncContactsResource
    from .resources.typing_indicators import TypingIndicatorsResource, AsyncTypingIndicatorsResource

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

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def groups(self) -> GroupsResource:
        from .resources.groups import GroupsResource

        return GroupsResource(self)

    @cached_property
    def media_objects(self) -> MediaObjectsResource:
        from .resources.media_objects import MediaObjectsResource

        return MediaObjectsResource(self)

    @cached_property
    def lookups(self) -> LookupsResource:
        from .resources.lookups import LookupsResource

        return LookupsResource(self)

    @cached_property
    def typing_indicators(self) -> TypingIndicatorsResource:
        from .resources.typing_indicators import TypingIndicatorsResource

        return TypingIndicatorsResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> SendblueAPIWithRawResponse:
        return SendblueAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendblueAPIWithStreamedResponse:
        return SendblueAPIWithStreamedResponse(self)

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

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        from .resources.groups import AsyncGroupsResource

        return AsyncGroupsResource(self)

    @cached_property
    def media_objects(self) -> AsyncMediaObjectsResource:
        from .resources.media_objects import AsyncMediaObjectsResource

        return AsyncMediaObjectsResource(self)

    @cached_property
    def lookups(self) -> AsyncLookupsResource:
        from .resources.lookups import AsyncLookupsResource

        return AsyncLookupsResource(self)

    @cached_property
    def typing_indicators(self) -> AsyncTypingIndicatorsResource:
        from .resources.typing_indicators import AsyncTypingIndicatorsResource

        return AsyncTypingIndicatorsResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSendblueAPIWithRawResponse:
        return AsyncSendblueAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendblueAPIWithStreamedResponse:
        return AsyncSendblueAPIWithStreamedResponse(self)

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
    _client: SendblueAPI

    def __init__(self, client: SendblueAPI) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithRawResponse:
        from .resources.groups import GroupsResourceWithRawResponse

        return GroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def media_objects(self) -> media_objects.MediaObjectsResourceWithRawResponse:
        from .resources.media_objects import MediaObjectsResourceWithRawResponse

        return MediaObjectsResourceWithRawResponse(self._client.media_objects)

    @cached_property
    def lookups(self) -> lookups.LookupsResourceWithRawResponse:
        from .resources.lookups import LookupsResourceWithRawResponse

        return LookupsResourceWithRawResponse(self._client.lookups)

    @cached_property
    def typing_indicators(self) -> typing_indicators.TypingIndicatorsResourceWithRawResponse:
        from .resources.typing_indicators import TypingIndicatorsResourceWithRawResponse

        return TypingIndicatorsResourceWithRawResponse(self._client.typing_indicators)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncSendblueAPIWithRawResponse:
    _client: AsyncSendblueAPI

    def __init__(self, client: AsyncSendblueAPI) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithRawResponse:
        from .resources.groups import AsyncGroupsResourceWithRawResponse

        return AsyncGroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def media_objects(self) -> media_objects.AsyncMediaObjectsResourceWithRawResponse:
        from .resources.media_objects import AsyncMediaObjectsResourceWithRawResponse

        return AsyncMediaObjectsResourceWithRawResponse(self._client.media_objects)

    @cached_property
    def lookups(self) -> lookups.AsyncLookupsResourceWithRawResponse:
        from .resources.lookups import AsyncLookupsResourceWithRawResponse

        return AsyncLookupsResourceWithRawResponse(self._client.lookups)

    @cached_property
    def typing_indicators(self) -> typing_indicators.AsyncTypingIndicatorsResourceWithRawResponse:
        from .resources.typing_indicators import AsyncTypingIndicatorsResourceWithRawResponse

        return AsyncTypingIndicatorsResourceWithRawResponse(self._client.typing_indicators)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class SendblueAPIWithStreamedResponse:
    _client: SendblueAPI

    def __init__(self, client: SendblueAPI) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithStreamingResponse:
        from .resources.groups import GroupsResourceWithStreamingResponse

        return GroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def media_objects(self) -> media_objects.MediaObjectsResourceWithStreamingResponse:
        from .resources.media_objects import MediaObjectsResourceWithStreamingResponse

        return MediaObjectsResourceWithStreamingResponse(self._client.media_objects)

    @cached_property
    def lookups(self) -> lookups.LookupsResourceWithStreamingResponse:
        from .resources.lookups import LookupsResourceWithStreamingResponse

        return LookupsResourceWithStreamingResponse(self._client.lookups)

    @cached_property
    def typing_indicators(self) -> typing_indicators.TypingIndicatorsResourceWithStreamingResponse:
        from .resources.typing_indicators import TypingIndicatorsResourceWithStreamingResponse

        return TypingIndicatorsResourceWithStreamingResponse(self._client.typing_indicators)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncSendblueAPIWithStreamedResponse:
    _client: AsyncSendblueAPI

    def __init__(self, client: AsyncSendblueAPI) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithStreamingResponse:
        from .resources.groups import AsyncGroupsResourceWithStreamingResponse

        return AsyncGroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def media_objects(self) -> media_objects.AsyncMediaObjectsResourceWithStreamingResponse:
        from .resources.media_objects import AsyncMediaObjectsResourceWithStreamingResponse

        return AsyncMediaObjectsResourceWithStreamingResponse(self._client.media_objects)

    @cached_property
    def lookups(self) -> lookups.AsyncLookupsResourceWithStreamingResponse:
        from .resources.lookups import AsyncLookupsResourceWithStreamingResponse

        return AsyncLookupsResourceWithStreamingResponse(self._client.lookups)

    @cached_property
    def typing_indicators(self) -> typing_indicators.AsyncTypingIndicatorsResourceWithStreamingResponse:
        from .resources.typing_indicators import AsyncTypingIndicatorsResourceWithStreamingResponse

        return AsyncTypingIndicatorsResourceWithStreamingResponse(self._client.typing_indicators)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = SendblueAPI

AsyncClient = AsyncSendblueAPI
