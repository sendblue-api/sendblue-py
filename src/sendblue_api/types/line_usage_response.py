# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .line_usage_snapshot import LineUsageSnapshot

__all__ = [
    "LineUsageResponse",
    "Pacing",
    "PacingLine",
    "PacingLineBurst",
    "PacingLineCold",
    "PacingLineNewContacts",
    "PacingLineTotal",
    "PacingLineWarm",
]


class PacingLineBurst(BaseModel):
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    limit: float

    remaining: int

    suggested_delay_ms: int = FieldInfo(alias="suggestedDelayMs")


class PacingLineCold(BaseModel):
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    limit: float

    remaining: int

    suggested_delay_ms: int = FieldInfo(alias="suggestedDelayMs")


class PacingLineNewContacts(BaseModel):
    remaining: int

    resets_at: datetime = FieldInfo(alias="resetsAt")


class PacingLineTotal(BaseModel):
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    limit: float

    remaining: int

    suggested_delay_ms: int = FieldInfo(alias="suggestedDelayMs")


class PacingLineWarm(BaseModel):
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    limit: float

    remaining: int

    suggested_delay_ms: int = FieldInfo(alias="suggestedDelayMs")


class PacingLine(BaseModel):
    burst: Optional[PacingLineBurst] = None
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    cold: Optional[PacingLineCold] = None
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    new_contacts: Optional[PacingLineNewContacts] = FieldInfo(alias="newContacts", default=None)

    phone: str

    sampled_at: Optional[datetime] = FieldInfo(alias="sampledAt", default=None)

    state: Literal["ready", "unknown", "stale", "unavailable"]

    total: Optional[PacingLineTotal] = None
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """

    warm: Optional[PacingLineWarm] = None
    """Continuously refilling provisional message budget.

    Null means observation coverage is incomplete or stale; it never means zero.
    """


class Pacing(BaseModel):
    """Independently enrolled advisory pacing.

    May be present when enforced capacity enabled is false. Omitted when pacing is disabled.
    """

    enabled: bool

    lines: List[PacingLine]

    unavailable: bool

    version: Literal[1]


class LineUsageResponse(BaseModel):
    enabled: bool
    """Whether usage reporting is enabled for your account.

    When false, lines is empty.
    """

    lines: List[LineUsageSnapshot]

    status: Literal["OK"]

    pacing: Optional[Pacing] = None
    """Independently enrolled advisory pacing.

    May be present when enforced capacity enabled is false. Omitted when pacing is
    disabled.
    """
