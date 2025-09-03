# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["GroupSendMessageParams"]


class GroupSendMessageParams(TypedDict, total=False):
    content: Required[str]
    """Message text content"""

    from_number: Required[str]
    """**REQUIRED** - The phone number to send from.

    Must be one of your registered Sendblue phone numbers in E.164 format. Without
    this parameter, the message will fail to send.
    """

    group_id: str
    """Unique identifier for an existing group"""

    media_url: str
    """URL of media file to send"""

    numbers: SequenceNotStr[str]
    """Array of recipient phone numbers in E.164 format"""
