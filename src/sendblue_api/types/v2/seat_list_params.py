# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SeatListParams"]


class SeatListParams(TypedDict, total=False):
    email: str
    """Optional exact-match filter on seat email"""

    limit: int
    """Maximum number of seats to return"""

    offset: int
    """Number of seats to skip"""
