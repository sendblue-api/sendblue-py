# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VerificationState"]


class VerificationState(BaseModel):
    channel: str

    date_created: datetime

    date_updated: datetime

    service_sid: str

    sid: str

    status: str

    date_completed: Optional[datetime] = None

    to: Optional[str] = None
