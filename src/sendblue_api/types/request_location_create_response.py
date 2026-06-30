# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequestLocationCreateResponse"]


class RequestLocationCreateResponse(BaseModel):
    message: Optional[str] = None

    message_handle: Optional[str] = None
    """Unique identifier for tracking the request message"""

    number: Optional[str] = None
    """Recipient phone number"""

    status: Optional[Literal["QUEUED"]] = None

    uuid: Optional[str] = None
    """Unique identifier for tracking the request message"""
