# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageResponse", "Location"]


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
