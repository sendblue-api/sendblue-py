# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactOptOutParams"]


class ContactOptOutParams(TypedDict, total=False):
    number: Required[str]
    """Phone number in E.164 format"""

    opted_out: bool
    """Set to false to opt the contact back in (defaults to true)"""
