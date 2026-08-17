# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .verification_state import VerificationState

__all__ = ["VerificationListResponse", "Pagination"]


class Pagination(BaseModel):
    count: Optional[int] = None

    has_more: Optional[bool] = None

    limit: Optional[int] = None

    offset: Optional[int] = None


class VerificationListResponse(BaseModel):
    data: List[VerificationState]

    pagination: Pagination

    status: Literal["OK"]
