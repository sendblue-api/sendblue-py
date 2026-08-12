# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerifiedContactCreateResponse", "Data", "DataContact", "DataLine"]


class DataContact(BaseModel):
    created_at: datetime

    phone_number: str
    """Contact phone number in E.164 format"""

    updated_at: datetime

    verification_status: Literal["pending", "verified"]

    verified: bool
    """Whether this contact has completed verification by messaging the shared line"""


class DataLine(BaseModel):
    phone_number: Optional[str] = None
    """Shared Sendblue line the contact must message to complete verification"""

    type: Literal["shared"]


class Data(BaseModel):
    contact: DataContact

    line: Optional[DataLine] = None

    verification_instructions: Optional[str] = None
    """Null when the contact is already verified"""


class VerifiedContactCreateResponse(BaseModel):
    data: Optional[Data] = None
