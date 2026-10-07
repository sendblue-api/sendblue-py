# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LineUsageWindow"]


class LineUsageWindow(BaseModel):
    limit: Optional[float] = None
    """Current limit with any account or line overrides."""

    next_slot_at: Optional[datetime] = FieldInfo(alias="nextSlotAt", default=None)
    """When the oldest counted contact leaves this window.

    If the limit was lowered below usage, use availableAt to decide when to retry.
    """

    remaining: Optional[int] = None
    """New contacts you can still message in this window.

    Zero if current usage exceeds a lowered limit.
    """

    used: Optional[int] = None
    """Number of new contacts counted in this window."""
