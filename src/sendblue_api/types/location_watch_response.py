# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LocationWatchResponse", "Location"]


class Location(BaseModel):
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


class LocationWatchResponse(BaseModel):
    """JSON data payload from one named event in a live-location SSE stream"""

    from_number: Optional[str] = None
    """Sendblue line receiving the shared location"""

    location: Optional[Location] = None

    message: Optional[str] = None
    """Human-readable watch failure"""

    number: Optional[str] = None
    """Contact whose location is being watched or changed"""

    reason: Optional[str] = None
    """Why the stream ended normally.

    Known values are `sharing_ended`, `authorization_revoked`,
    `worker_disconnected`, and `watch_ended`. Clients should tolerate additional
    values.
    """

    state: Optional[Literal["not_shared", "shared_no_fix_yet", "shared_with_fix"]] = None

    status: Optional[Literal["OK", "ERROR"]] = None
