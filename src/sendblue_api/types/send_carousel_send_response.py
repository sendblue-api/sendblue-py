# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SendCarouselSendResponse", "ReplyTo", "ThreadOriginator"]


class ReplyTo(BaseModel):
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same
    account, conversation, and sending line.
    """

    message_handle: str
    """Public handle of the immediate parent message"""

    part_index: Optional[int] = None
    """Advanced override for a known part of a multipart target.

    Omit this in normal reply requests and never guess it; requests default to 0.
    When replying to an attachment represented by its own webhook, use that
    webhook's `message_handle` and omit `part_index` so Sendblue can use the stored
    authoritative part. Responses omit it when no authoritative immediate-parent
    part is available.
    """


class ThreadOriginator(BaseModel):
    """Message that originated an iMessage inline-reply thread."""

    message_handle: str
    """Public handle of the thread's root message"""

    part: Optional[str] = None
    """Opaque Apple thread-originator part descriptor"""


class SendCarouselSendResponse(BaseModel):
    account_email: Optional[str] = FieldInfo(alias="accountEmail", default=None)
    """Email of the account that sent the message"""

    from_number: Optional[str] = None
    """Sending phone number"""

    is_outbound: Optional[bool] = None

    media_url: Optional[str] = None
    """First media URL from the carousel"""

    message_handle: Optional[str] = None
    """Unique identifier for tracking the message"""

    message_type: Optional[str] = None

    number: Optional[str] = None
    """Recipient phone number"""

    reply_to: Optional[ReplyTo] = None
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same account, conversation, and sending line.
    """

    status: Optional[str] = None

    thread_originator: Optional[ThreadOriginator] = None
    """Message that originated an iMessage inline-reply thread."""
