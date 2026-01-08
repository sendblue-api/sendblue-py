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
    "WebhooksLineAssigned",
    "WebhooksLineBlocked",
    "WebhooksOutbound",
    "WebhooksReceive",
]


class WebhookUpdateParams(TypedDict, total=False):
    webhooks: Required[Webhooks]


WebhooksLineAssigned: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksLineBlocked: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksOutbound: TypeAlias = Union[str, WebhookConfigurationParam]

WebhooksReceive: TypeAlias = Union[str, WebhookConfigurationParam]


class Webhooks(TypedDict, total=False):
    global_secret: Annotated[str, PropertyInfo(alias="globalSecret")]
    """Global secret applied to all webhooks"""

    line_assigned: SequenceNotStr[WebhooksLineAssigned]
    """Webhooks for line assigned events"""

    line_blocked: SequenceNotStr[WebhooksLineBlocked]
    """Webhooks for line blocked events"""

    outbound: SequenceNotStr[WebhooksOutbound]
    """Webhooks for outbound message events"""

    receive: SequenceNotStr[WebhooksReceive]
    """Webhooks for inbound message events"""
