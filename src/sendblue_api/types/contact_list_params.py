# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    cid: str
    """Filter by contact ID"""

    limit: int
    """Maximum number of contacts to return"""

    offset: int
    """Number of contacts to skip"""

    order_by: str
    """Field to sort by"""

    order_direction: Literal["asc", "desc"]
    """Sort direction"""

    phone_number: str
    """Filter by phone number"""
