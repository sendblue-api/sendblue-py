# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TypingIndicatorSendResponse"]


class TypingIndicatorSendResponse(BaseModel):
    error_message: Optional[str] = None
    """The error message if the status is ERROR"""

    number: Optional[str] = None
    """The number you evaluated in E.164 format"""

    status: Optional[Literal["SENT", "ERROR"]] = None
    """The status of the typing indicator you tried to send"""
