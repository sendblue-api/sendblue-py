# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookDeleteParams"]


class WebhookDeleteParams(TypedDict, total=False):
    webhooks: Required[SequenceNotStr[str]]
    """Array of webhook URLs to delete"""

    type: Literal["receive", "line_blocked", "line_assigned", "outbound"]
    """Type of webhook to delete from"""
