# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageResponse"]


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

    media_url: Optional[str] = None
    """URL of attached media"""

    message_handle: Optional[str] = None
    """Unique identifier for tracking the message"""

    number: Optional[str] = None
    """Recipient phone number"""

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

    status: Optional[Literal["QUEUED", "SENT", "DELIVERED", "READ", "ERROR"]] = None
