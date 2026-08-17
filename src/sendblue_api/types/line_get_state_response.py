# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .line_state import LineState

__all__ = ["LineGetStateResponse"]


class LineGetStateResponse(BaseModel):
    data: List[LineState]

    snapshot_at: datetime

    status: Literal["OK"]
