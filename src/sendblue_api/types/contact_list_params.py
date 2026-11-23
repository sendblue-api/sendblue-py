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

    cursor: str
    """Opaque next_cursor from the previous page. Also selects cursor pagination."""

    limit: int
    """Maximum contacts to return.

    Default 100; capped at 1000 in both legacy and cursor mode.
    """

    offset: int
    """Number of contacts to skip.

    Above 10000 returns 400. Cannot be combined with cursor mode.
    """

    order_by: Literal["created_at", "firstName", "lastName", "phone"]
    """Field to sort by; cursor mode permits only created_at."""

    order_direction: Literal["asc", "desc"]
    """Sort direction; cursor mode permits only desc."""

    pagination: Literal["cursor"]
    """Select cursor pagination and its response envelope."""

    phone_number: str
    """Filter by phone number"""
