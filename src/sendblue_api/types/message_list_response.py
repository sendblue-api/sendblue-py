# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageListResponse", "Data", "DataLocation", "DataReplyTo", "DataThreadOriginator", "Pagination"]


class DataLocation(BaseModel):
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


class DataReplyTo(BaseModel):
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


class DataThreadOriginator(BaseModel):
    """Message that originated an iMessage inline-reply thread."""

    message_handle: str
    """Public handle of the thread's root message"""

    part: Optional[str] = None
    """Opaque Apple thread-originator part descriptor"""


class Data(BaseModel):
    account_email: Optional[str] = FieldInfo(alias="accountEmail", default=None)
    """Email of the account"""

    content: Optional[str] = None
    """Message content"""

    date_sent: Optional[datetime] = None
    """When the message was sent"""

    date_updated: Optional[datetime] = None
    """When the message was last updated"""

    error_code: Optional[int] = None
    """Numeric error code if message failed"""

    error_detail: Optional[str] = None
    """Detailed error information"""

    error_message: Optional[str] = None
    """Error message if message failed"""

    error_reason: Optional[str] = None
    """Error reason if message failed"""

    from_number: Optional[str] = None
    """Sender phone number"""

    group_display_name: Optional[str] = None
    """Display name for group messages"""

    group_id: Optional[str] = None
    """Group ID for group messages"""

    is_outbound: Optional[bool] = None
    """Whether this is an outbound message"""

    location: Optional[DataLocation] = None
    """Decoded Find My location share coordinates."""

    media_url: Optional[str] = None
    """URL of attached media"""

    message_handle: Optional[str] = None
    """Unique message identifier"""

    message_type: Optional[Literal["message", "group", "location"]] = None

    number: Optional[str] = None
    """Primary phone number (to_number for outbound, from_number for inbound)"""

    opted_out: Optional[bool] = None
    """Whether the recipient has opted out"""

    participants: Optional[List[str]] = None
    """List of participants for group messages"""

    plan: Optional[str] = None
    """Account plan used for this message"""

    reply_to: Optional[DataReplyTo] = None
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

    sendblue_number: Optional[str] = None
    """Sendblue phone number used"""

    sender_email: Optional[str] = None
    """Email of the seat (user) that sent the message.

    Auto-populated when a `seat_id` is provided on send. `null` for messages sent
    without a `seat_id`.
    """

    service: Optional[Literal["iMessage", "SMS", "RCS"]] = None
    """The messaging service used"""

    status: Optional[
        Literal[
            "REGISTERED",
            "PENDING",
            "SENT",
            "DELIVERED",
            "RECEIVED",
            "QUEUED",
            "ERROR",
            "DECLINED",
            "ACCEPTED",
            "SUCCESS",
        ]
    ] = None

    thread_originator: Optional[DataThreadOriginator] = None
    """Message that originated an iMessage inline-reply thread."""

    to_number: Optional[str] = None
    """Recipient phone number"""

    was_downgraded: Optional[bool] = None
    """Whether the message was downgraded from iMessage to SMS"""


class Pagination(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more messages available"""

    limit: Optional[int] = None
    """Number of messages returned in this request"""

    offset: Optional[int] = None
    """Number of messages skipped"""

    total: Optional[int] = None
    """Total number of messages matching the filters"""


class MessageListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None

    status: Optional[str] = None
