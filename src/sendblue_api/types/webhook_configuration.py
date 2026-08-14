# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebhookConfiguration"]


class WebhookConfiguration(BaseModel):
    url: str
    """Webhook endpoint URL for receiving callbacks"""

    secret: Optional[str] = None
    """Secret for webhook signature verification"""

    sendblue_numbers: Optional[List[str]] = None
    """Receive webhooks only.

    When present, only inbound messages received by these Sendblue line numbers are
    delivered to this webhook.
    """
