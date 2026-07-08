# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LocationListResponse", "Location", "LocationLocation"]


class LocationLocation(BaseModel):
    accuracy: Optional[float] = None

    address: Optional[str] = None

    altitude: Optional[float] = None

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    latitude: Optional[float] = None

    location_type: Optional[Literal["shallow", "live", "legacy", "unknown"]] = FieldInfo(
        alias="locationType", default=None
    )

    longitude: Optional[float] = None

    refresh_error: Optional[str] = FieldInfo(alias="refreshError", default=None)
    """Present when cached data is returned after a refresh error"""

    timestamp: Optional[datetime] = None


class Location(BaseModel):
    location: Optional[LocationLocation] = None

    number: Optional[str] = None

    state: Optional[Literal["not_shared", "shared_no_fix_yet", "shared_with_fix"]] = None


class LocationListResponse(BaseModel):
    from_number: Optional[str] = None

    locations: Optional[List[Location]] = None

    status: Optional[Literal["OK"]] = None
