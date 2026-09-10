# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GroupPhoto"]


class GroupPhoto(BaseModel):
    photo_guid: str
    """Device-verified identifier of the current Apple group photo"""

    url: str
    """
    Direct URL for downloading the current photo; anyone with the exact URL can
    download it while the image exists
    """
