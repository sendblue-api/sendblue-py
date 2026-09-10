# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GroupSetPhotoParams"]


class GroupSetPhotoParams(TypedDict, total=False):
    photo_url: Required[Optional[str]]
    """
    Direct, publicly resolvable https URL of the image to set (JPEG, PNG, or GIF, at
    most 5 MB and 25 million aggregate decoded pixels; redirects are not followed);
    null clears the group photo
    """

    from_number: Optional[str]
    """
    Sendblue line that must perform the change; it must have an iMessage mapping for
    this group, and no other line is used if it cannot act. Omit or pass null for
    automatic selection
    """
