# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageResponse", "Location", "ReplyTo", "ThreadOriginator"]


class Location(BaseModel):
    """Decoded Find My location share coordinates."""

    latitude: float

    longitude: float

    accuracy: Optional[float] = None
    """Horizontal accuracy in meters"""

    altitude: Optional[float] = None
    """Altitude in meters"""

    duration: Optional[str] = None
    """Share duration selected by the recipient"""

    timestamp: Optional[datetime] = None


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


class MessageResponse(BaseModel):
    account_email: Optional[str] = None
    """Email of the account that sent the message"""

    content: Optional[str] = None
    """Message content"""

    date_created: Optional[datetime] = None
    """When the message was created"""

    date_updated: Optional[datetime] = None
    """When the message was last updated"""

    error_code: Optional[int] = None
    """Numeric error code if message failed"""

    error_message: Optional[str] = None
    """Error message if message failed"""

    from_number: Optional[str] = None
    """Sending phone number"""

    is_outbound: Optional[bool] = None
    """Whether this is an outbound message"""

    location: Optional[Location] = None
    """Decoded Find My location share coordinates."""

    media_url: Optional[str] = None
    """URL of attached media"""

    message_handle: Optional[str] = None
    """Unique identifier for tracking the message"""

    message_type: Optional[Literal["message", "group", "location"]] = None

    number: Optional[str] = None
    """Recipient phone number"""

    reply_to: Optional[ReplyTo] = None
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same account, conversation, and sending line.
    """

    seat_id: Optional[str] = None
    """UUID of the seat that sent the message.

    Present when `seat_id` was provided on send, or for dashboard-originated group
    messages.
    """

    send_style: Optional[
        Literal[
            "celebration",
            "shooting_star",
            "fireworks",
            "lasers",
            "love",
            "confetti",
            "balloons",
            "spotlight",
            "echo",
            "invisible",
            "gentle",
            "loud",
            "slam",
        ]
    ] = None
    """The iMessage expressive message style"""

    sender_email: Optional[str] = None
    """Email of the seat (user) that sent the message.

    Auto-populated when a `seat_id` is provided on send. `null` for messages sent
    without a `seat_id`.
    """

    status: Optional[Literal["QUEUED", "SENT", "DELIVERED", "ERROR"]] = None

    thread_originator: Optional[ThreadOriginator] = None
    """Message that originated an iMessage inline-reply thread."""
