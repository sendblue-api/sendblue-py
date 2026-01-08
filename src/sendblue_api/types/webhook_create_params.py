# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .webhook_configuration_param import WebhookConfigurationParam

__all__ = ["WebhookCreateParams", "Webhook"]


class WebhookCreateParams(TypedDict, total=False):
    webhooks: Required[SequenceNotStr[Webhook]]
    """Array of webhook URLs or webhook objects"""

    global_secret: Annotated[str, PropertyInfo(alias="globalSecret")]
    """Global secret for webhook signature verification"""

    type: Literal["receive", "line_blocked", "line_assigned", "outbound"]
    """Type of webhook to add"""


Webhook: TypeAlias = Union[str, WebhookConfigurationParam]
