# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WebhookConfiguration",
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


class CallLogWebhookObject(BaseModel):
    url: str
    """Webhook URL (HTTPS only)"""

    secret: Optional[str] = None
    """Secret for webhook verification"""


CallLog: TypeAlias = Union[str, CallLogWebhookObject]


class LineAssignedWebhookObject(BaseModel):
    url: str
    """Webhook URL (HTTPS only)"""

    secret: Optional[str] = None
    """Secret for webhook verification"""


LineAssigned: TypeAlias = Union[str, LineAssignedWebhookObject]


class LineBlockedWebhookObject(BaseModel):
    url: str
    """Webhook URL (HTTPS only)"""

    secret: Optional[str] = None
    """Secret for webhook verification"""


LineBlocked: TypeAlias = Union[str, LineBlockedWebhookObject]


class OutboundWebhookObject(BaseModel):
    url: str
    """Webhook URL (HTTPS only)"""

    secret: Optional[str] = None
    """Secret for webhook verification"""


Outbound: TypeAlias = Union[str, OutboundWebhookObject]


class ReceiveWebhookObject(BaseModel):
    url: str
    """Webhook URL (HTTPS only)"""

    secret: Optional[str] = None
    """Secret for webhook verification"""


Receive: TypeAlias = Union[str, ReceiveWebhookObject]


class WebhookConfiguration(BaseModel):
    call_log: Optional[List[CallLog]] = None
    """Webhooks for call logs"""

    contact_created: Optional[List[str]] = None
    """Webhooks for contact creation (URL strings only)"""

    global_secret: Optional[str] = FieldInfo(alias="globalSecret", default=None)
    """Global secret applied to all webhooks"""

    line_assigned: Optional[List[LineAssigned]] = None
    """Webhooks for line assignment"""

    line_blocked: Optional[List[LineBlocked]] = None
    """Webhooks for blocked lines"""

    outbound: Optional[List[Outbound]] = None
    """Webhooks for outbound messages"""

    receive: Optional[List[Receive]] = None
    """Webhooks for inbound messages"""

    secret: Optional[str] = None
    """Legacy secret field"""
