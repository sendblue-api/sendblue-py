# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LocationWatchParams"]


class LocationWatchParams(TypedDict, total=False):
    from_number: Required[str]
    """Your supported Sendblue number in E.164 format"""
