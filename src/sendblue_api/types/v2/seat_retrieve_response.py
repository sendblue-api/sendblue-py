# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SeatRetrieveResponse", "Seat"]


class Seat(BaseModel):
    account: Optional[str] = None
    """Account name the seat belongs to"""

    created_at: Optional[datetime] = None
    """When the seat was created"""

    email: Optional[str] = None
    """Email address of the seat user"""

    first_name: Optional[str] = None
    """First name"""

    forwarding_number: Optional[str] = None
    """Optional phone number used to forward calls"""

    last_name: Optional[str] = None
    """Last name"""

    seat_id: Optional[str] = None
    """Primary identifier for the seat.

    Pass this on the send endpoints' `seat_id` parameter.
    """


class SeatRetrieveResponse(BaseModel):
    seat: Optional[Seat] = None

    status: Optional[str] = None
