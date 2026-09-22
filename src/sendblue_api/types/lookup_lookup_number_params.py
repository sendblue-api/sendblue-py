# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LookupLookupNumberParams"]


class LookupLookupNumberParams(TypedDict, total=False):
    number: Required[str]
    """The phone number in E.164 format or email address to evaluate"""
