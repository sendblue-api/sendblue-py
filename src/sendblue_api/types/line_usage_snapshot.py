# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .line_usage_window import LineUsageWindow
from .line_usage_daily_window import LineUsageDailyWindow

__all__ = ["LineUsageSnapshot"]


class LineUsageSnapshot(BaseModel):
    available_at: Optional[datetime] = FieldInfo(alias="availableAt", default=None)
    """
    When a limited line is expected to have capacity in both windows, assuming no
    further sends. Null if the line is not limited or the time is unknown.
    """

    daily: LineUsageDailyWindow

    hourly: LineUsageWindow

    phone: str
    """The account's Sendblue phone line in E.164 format."""

    sampled_at: datetime = FieldInfo(alias="sampledAt")

    state: Literal["available", "limited", "paused", "not_applicable", "unavailable"]
    """Current capacity status.

    Paused means the daily limit is zero; not_applicable means these limits do not
    apply; unavailable means usage or settings could not be checked.
    """

    new_contact_lookback_days: Optional[float] = FieldInfo(alias="newContactLookbackDays", default=None)
    """Days without activity before a contact counts as new again.

    This field may be omitted.
    """
