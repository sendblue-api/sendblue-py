# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .line_usage_window import LineUsageWindow

__all__ = ["LineUsageDailyWindow"]


class LineUsageDailyWindow(LineUsageWindow):
    resets_at: Optional[datetime] = FieldInfo(alias="resetsAt", default=None)
    """
    Next daily reset at 3 AM ET (America/New_York), accounting for daylight saving
    time.
    """
