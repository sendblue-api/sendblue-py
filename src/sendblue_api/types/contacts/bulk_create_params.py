# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BulkCreateParams", "Contact"]


class BulkCreateParams(TypedDict, total=False):
    contacts: Required[Iterable[Contact]]


class Contact(TypedDict, total=False):
    phone: Required[str]

    company: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    tags: List[str]
