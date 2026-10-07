# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LineContactStatusResponse"]


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
