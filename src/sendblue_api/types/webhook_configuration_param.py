# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebhookConfigurationParam"]


class WebhookConfigurationParam(TypedDict, total=False):
    url: Required[str]
    """Webhook endpoint URL for receiving callbacks"""

    secret: str
    """Secret for webhook signature verification"""
