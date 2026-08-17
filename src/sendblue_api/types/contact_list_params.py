# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    cid: str
    """Filter by contact ID"""

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter contacts created at or after this ISO 8601 timestamp (event recovery)"""

    limit: int
    """Maximum number of contacts to return. Defaults to 100, capped at 1000."""

    offset: int
    """Number of contacts to skip. Capped at 10000."""

    order_by: str
    """Field to sort by"""

    order_direction: Literal["asc", "desc"]
    """Sort direction"""

    phone_number: str
    """Filter by phone number"""
