# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LineContactStatusResponse", "Pacing", "PacingWarning"]


class PacingWarning(BaseModel):
    """Optional advice for subsequent non-active one-to-one iMessage sends.

    Never a retry instruction or an admission decision.
    """

    expires_at: datetime

    reasons: List[Literal["warm_hourly", "cold_hourly", "line_hourly", "line_burst", "new_contacts_daily"]]

    version: Literal[1]

    new_contacts_remaining: Optional[Literal[0]] = None

    new_contacts_reset_at: Optional[datetime] = None

    suggested_delay_ms: Optional[int] = None


class Pacing(BaseModel):
    activity: Literal["active", "warm", "cold", "unknown"]

    service: Literal["iMessage"]

    version: Literal[1]

    warning: Optional[PacingWarning] = None
    """Optional advice for subsequent non-active one-to-one iMessage sends.

    Never a retry instruction or an admission decision.
    """


class LineContactStatusResponse(BaseModel):
    classification: Literal["known", "new", "not_applicable", "unavailable"]
    """Known or new contact status.

    Returns not_applicable if these limits do not apply, or unavailable if Sendblue
    could not check the status.
    """

    known_contact: Optional[bool] = None
    """True for known, false for new, and null for not_applicable or unavailable.

    Other sending rules still apply.
    """

    new_contact_lookback_days: Optional[float] = None
    """Days without activity before a contact counts as new again.

    Null if this limit does not apply or the setting is unavailable.
    """

    number: str
    """Contact phone number in E.164 format."""

    sampled_at: datetime
    """When the contact status was checked in ISO 8601 UTC."""

    sendblue_number: str
    """Sendblue phone number in E.164 format."""

    status: Literal["OK"]

    pacing: Optional[Pacing] = None
