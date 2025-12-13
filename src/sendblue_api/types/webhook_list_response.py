# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .webhook_configuration import WebhookConfiguration

__all__ = [
    "WebhookListResponse",
    "Webhooks",
    "WebhooksCallLog",
    "WebhooksLineAssigned",
    "WebhooksLineBlocked",
    "WebhooksOutbound",
    "WebhooksReceive",
]

WebhooksCallLog: TypeAlias = Union[str, WebhookConfiguration]

WebhooksLineAssigned: TypeAlias = Union[str, WebhookConfiguration]

WebhooksLineBlocked: TypeAlias = Union[str, WebhookConfiguration]

WebhooksOutbound: TypeAlias = Union[str, WebhookConfiguration]

WebhooksReceive: TypeAlias = Union[str, WebhookConfiguration]


class Webhooks(BaseModel):
    call_log: Optional[List[WebhooksCallLog]] = None
    """Webhooks for call log events"""

    contact_created: Optional[List[str]] = None
    """Webhooks for contact created events"""

    global_secret: Optional[str] = FieldInfo(alias="globalSecret", default=None)
    """Global secret applied to all webhooks"""

    line_assigned: Optional[List[WebhooksLineAssigned]] = None
    """Webhooks for line assigned events"""

    line_blocked: Optional[List[WebhooksLineBlocked]] = None
    """Webhooks for line blocked events"""

    outbound: Optional[List[WebhooksOutbound]] = None
    """Webhooks for outbound message events"""

    receive: Optional[List[WebhooksReceive]] = None
    """Webhooks for inbound message events"""


class WebhookListResponse(BaseModel):
    status: Optional[str] = None

    webhooks: Optional[Webhooks] = None
