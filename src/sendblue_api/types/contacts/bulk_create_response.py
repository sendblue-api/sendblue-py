# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..contact import Contact
from ..._models import BaseModel

__all__ = ["BulkCreateResponse", "Failure"]


class Failure(BaseModel):
    contact: Dict[str, object]
    """The submitted contact item that failed."""

    error: str
    """Per-item failure message."""


class BulkCreateResponse(BaseModel):
    contacts: Optional[List[Contact]] = None

    failures: Optional[List[Failure]] = None
    """Present when one or more items fail.

    An acknowledgment failure can follow a committed creation or update.
    """

    number_of_contacts_created: Optional[int] = FieldInfo(alias="numberOfContactsCreated", default=None)
    """Number of successfully acknowledged items returned in contacts."""

    status: Optional[str] = None
