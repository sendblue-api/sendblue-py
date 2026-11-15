# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContactLookupResponse", "Contact"]


class Contact(BaseModel):
    contact_id: str

    phone: str

    tags: List[str]


class ContactLookupResponse(BaseModel):
    contacts: List[Contact]

    not_found: List[str]

    status: Literal["OK"]
