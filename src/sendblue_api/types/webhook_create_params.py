# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams", "Webhook", "WebhookWebhookObject"]


class WebhookCreateParams(TypedDict, total=False):
    webhooks: Required[SequenceNotStr[Webhook]]
    """Array of webhook URLs or webhook objects to add"""

    global_secret: Annotated[str, PropertyInfo(alias="globalSecret")]
    """Optional global secret to apply to all webhooks"""

    type: Literal["receive", "call_log", "line_blocked", "line_assigned", "outbound", "contact_created"]
    """Webhook type (default to 'receive')"""


class WebhookWebhookObject(TypedDict, total=False):
    url: Required[str]
    """Webhook URL (HTTPS only)"""

    secret: str
    """Secret for webhook verification"""


Webhook: TypeAlias = Union[str, WebhookWebhookObject]
