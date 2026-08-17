# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LineState"]


class LineState(BaseModel):
    assignment: Literal["assigned", "shared", "grace_period"]

    sendblue_number: Optional[str] = None

    status: Literal["ONLINE", "OFFLINE", "DEGRADED", "UNKNOWN"]

    worker_id: str

    degraded_since: Optional[datetime] = None

    effective_until: Optional[datetime] = None

    status_changed_at: Optional[datetime] = None
