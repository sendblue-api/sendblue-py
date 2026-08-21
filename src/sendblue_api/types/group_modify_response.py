# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GroupModifyResponse"]


class GroupModifyResponse(BaseModel):
    error: Optional[str] = None

    error_message: Optional[str] = None

    group_id: Optional[str] = None

    modify_type: Optional[str] = None

    number: Optional[str] = None

    status: Optional[str] = None
