# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .webhook_configuration_param import WebhookConfigurationParam

__all__ = [
    "WebhookUpdateParams",
    "Webhooks",
    "WebhooksCallLog",
    "WebhooksContactCreated",
    "WebhooksContactProfile",
    "WebhooksInboundCall",
    "WebhooksLineAssigned",
    "WebhooksLineBlocked",
    "WebhooksOutbound",
    "WebhooksReceive",
    "WebhooksTypingIndicator",
]


class WebhookUpdateParams(TypedDict, total=False):
    webhooks: Required[Webhooks]


WebhooksCallLog: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksContactCreated: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksContactProfile: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksInboundCall: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksLineAssigned: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksLineBlocked: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksOutbound: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksReceive: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksTypingIndicator: TypeAlias = Union[str, WebhookConfigurationParam]


class Webhooks(TypedDict, total=False):
    call_log: SequenceNotStr[WebhooksCallLog]
    """Webhooks for call log events"""

    contact_created: SequenceNotStr[WebhooksContactCreated]
    """Webhooks for contact created events"""

    contact_profile: SequenceNotStr[WebhooksContactProfile]
    """Webhooks for durable contact-profile publication completion and failure events"""

    global_secret: Annotated[str, PropertyInfo(alias="globalSecret")]
    """Global secret applied to all webhooks"""

    inbound_call: SequenceNotStr[WebhooksInboundCall]
    """Webhooks for inbound call events"""

    line_assigned: SequenceNotStr[WebhooksLineAssigned]
    """Webhooks for line assigned events"""

    line_blocked: SequenceNotStr[WebhooksLineBlocked]
    """Webhooks for line blocked events"""

    outbound: SequenceNotStr[WebhooksOutbound]
    """Webhooks for outbound message status updates"""

    receive: SequenceNotStr[WebhooksReceive]
    """Webhooks for inbound message events"""

    typing_indicator: SequenceNotStr[WebhooksTypingIndicator]
    """Webhooks for typing indicator events"""
