# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .contact import Contact
from .._models import BaseModel

__all__ = ["ContactCreateResponse"]


class ContactCreateResponse(BaseModel):
    contact: Optional[Contact] = None

    status: Optional[str] = None
