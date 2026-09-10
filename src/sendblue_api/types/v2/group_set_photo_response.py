# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..group_photo import GroupPhoto

__all__ = ["GroupSetPhotoResponse", "Data"]


class Data(BaseModel):
    from_number: Optional[str] = None
    """Sendblue line that performed the change"""

    group_id: str

    group_photo: Optional[GroupPhoto] = None
    """Device-verified current photo; null after a verified clear"""


class GroupSetPhotoResponse(BaseModel):
    data: Data

    status: Literal["OK"]
