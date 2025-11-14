# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WebhookConfigurationParam",
    "CallLog",
    "CallLogWebhookObject",
    "LineAssigned",
    "LineAssignedWebhookObject",
    "LineBlocked",
    "LineBlockedWebhookObject",
    "Outbound",
    "OutboundWebhookObject",
    "Receive",
    "ReceiveWebhookObject",
]


class CallLogWebhookObject(TypedDict, total=False):
    url: Required[str]
    """Webhook URL (HTTPS only)"""

    secret: str
    """Secret for webhook verification"""


CallLog: TypeAlias = Union[str, CallLogWebhookObject]


class LineAssignedWebhookObject(TypedDict, total=False):
    url: Required[str]
    """Webhook URL (HTTPS only)"""

    secret: str
    """Secret for webhook verification"""


LineAssigned: TypeAlias = Union[str, LineAssignedWebhookObject]


class LineBlockedWebhookObject(TypedDict, total=False):
    url: Required[str]
    """Webhook URL (HTTPS only)"""

    secret: str
    """Secret for webhook verification"""


LineBlocked: TypeAlias = Union[str, LineBlockedWebhookObject]


class OutboundWebhookObject(TypedDict, total=False):
    url: Required[str]
    """Webhook URL (HTTPS only)"""

    secret: str
    """Secret for webhook verification"""


Outbound: TypeAlias = Union[str, OutboundWebhookObject]


class ReceiveWebhookObject(TypedDict, total=False):
    url: Required[str]
    """Webhook URL (HTTPS only)"""

    secret: str
    """Secret for webhook verification"""


Receive: TypeAlias = Union[str, ReceiveWebhookObject]


class WebhookConfigurationParam(TypedDict, total=False):
    call_log: SequenceNotStr[CallLog]
    """Webhooks for call logs"""

    contact_created: SequenceNotStr[str]
    """Webhooks for contact creation (URL strings only)"""

    global_secret: Annotated[str, PropertyInfo(alias="globalSecret")]
    """Global secret applied to all webhooks"""

    line_assigned: SequenceNotStr[LineAssigned]
    """Webhooks for line assignment"""

    line_blocked: SequenceNotStr[LineBlocked]
    """Webhooks for blocked lines"""

    outbound: SequenceNotStr[Outbound]
    """Webhooks for outbound messages"""

    receive: SequenceNotStr[Receive]
    """Webhooks for inbound messages"""

    secret: str
    """Legacy secret field"""
