# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .line_usage_snapshot import LineUsageSnapshot

__all__ = ["LineUsageResponse"]


class LineUsageResponse(BaseModel):
    enabled: bool
    """Whether usage reporting is enabled for your account.

    When false, lines is empty.
    """

    lines: List[LineUsageSnapshot]

    status: Literal["OK"]
