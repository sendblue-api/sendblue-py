# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ContactOptOutResponse"]


class ContactOptOutResponse(BaseModel):
    number: Optional[str] = None
    """The normalized phone number"""

    opted_out: Optional[bool] = None
    """The current opt-out status"""

    status: Optional[str] = None
