# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountEvent"]


class AccountEvent(BaseModel):
    id: str

    data: Dict[str, object]

    occurred_at: datetime

    type: Literal[
        "message.received",
        "message.created",
        "message.updated",
        "typing.changed",
        "line.assigned",
        "line.unassigned",
        "line.status.changed",
        "line.blocked",
        "contact.created",
        "verification.approved",
        "verification.expired",
        "verification.canceled",
    ]

    version: Literal[1]
