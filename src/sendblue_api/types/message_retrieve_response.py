# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageRetrieveResponse", "Data"]


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

    media_url: Optional[str] = None
    """URL of attached media"""

    message_handle: Optional[str] = None
    """Unique message identifier"""

    message_type: Optional[Literal["message", "group"]] = None

    number: Optional[str] = None
    """Primary phone number (to_number for outbound, from_number for inbound)"""

    opted_out: Optional[bool] = None
    """Whether the recipient has opted out"""

    participants: Optional[List[str]] = None
    """List of participants for group messages"""

    plan: Optional[str] = None
    """Account plan used for this message"""

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

    service: Optional[Literal["iMessage", "SMS"]] = None

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

    to_number: Optional[str] = None
    """Recipient phone number"""

    was_downgraded: Optional[bool] = None
    """Whether the message was downgraded from iMessage to SMS"""


class MessageRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    status: Optional[str] = None
