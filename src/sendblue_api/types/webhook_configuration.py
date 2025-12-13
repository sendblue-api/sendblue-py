# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookConfiguration"]


class WebhookConfiguration(BaseModel):
    url: str
    """Webhook endpoint URL for receiving callbacks"""

    secret: Optional[str] = None
    """Secret for webhook signature verification"""
