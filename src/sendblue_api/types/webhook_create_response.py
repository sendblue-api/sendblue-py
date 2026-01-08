# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .webhook_configuration import WebhookConfiguration

__all__ = [
    "WebhookCreateResponse",
    "Webhooks",
    "WebhooksLineAssigned",
    "WebhooksLineBlocked",
    "WebhooksOutbound",
    "WebhooksReceive",
]

WebhooksLineAssigned: TypeAlias = Union[str, WebhookConfiguration]

WebhooksLineBlocked: TypeAlias = Union[str, WebhookConfiguration]

WebhooksOutbound: TypeAlias = Union[str, WebhookConfiguration]

WebhooksReceive: TypeAlias = Union[str, WebhookConfiguration]


class Webhooks(BaseModel):
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


class WebhookCreateResponse(BaseModel):
    message: Optional[str] = None

    status: Optional[str] = None

    webhooks: Optional[Webhooks] = None
