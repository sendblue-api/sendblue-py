# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .contact import Contact
from .._models import BaseModel

__all__ = ["ContactListResponse", "UnionMember1"]


class UnionMember1(BaseModel):
    contacts: List[Contact]

    next_cursor: Optional[str] = None

    status: Literal["OK"]


ContactListResponse: TypeAlias = Union[List[Contact], UnionMember1]
