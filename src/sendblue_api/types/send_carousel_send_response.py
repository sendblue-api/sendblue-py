# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SendCarouselSendResponse"]


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

    status: Optional[str] = None
