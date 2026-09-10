# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LookupLookupNumberResponse"]


class LookupLookupNumberResponse(BaseModel):
    number: Optional[str] = None
    """The normalized phone number or email address evaluated"""

    service: Optional[Literal["iMessage", "SMS"]] = None
    """Whether iMessage support was detected"""
