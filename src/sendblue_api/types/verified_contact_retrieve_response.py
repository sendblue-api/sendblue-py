# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerifiedContactRetrieveResponse", "Data", "DataContact", "DataLine"]


class DataContact(BaseModel):
    id: int
    """Internal WorkerRoute identifier."""

    created_at: datetime

    phone_number: str
    """Contact phone number in E.164 format."""

    updated_at: datetime

    verification_status: Literal["pending", "verified"]

    verified: bool


class DataLine(BaseModel):
    phone_number: Optional[str] = None
    """Assigned Sendblue line in E.164 format."""

    type: Literal["shared"]


class Data(BaseModel):
    contact: DataContact

    line: Optional[DataLine] = None


class VerifiedContactRetrieveResponse(BaseModel):
    data: Optional[Data] = None
