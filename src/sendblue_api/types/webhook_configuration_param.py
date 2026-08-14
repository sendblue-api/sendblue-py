# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookConfigurationParam"]


class WebhookConfigurationParam(TypedDict, total=False):
    url: Required[str]
    """Webhook endpoint URL for receiving callbacks"""

    secret: str
    """Secret for webhook signature verification"""

    sendblue_numbers: SequenceNotStr[str]
    """Receive webhooks only.

    When present, only inbound messages received by these Sendblue line numbers are
    delivered to this webhook.
    """
