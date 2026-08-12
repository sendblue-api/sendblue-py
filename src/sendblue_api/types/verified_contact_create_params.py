# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerifiedContactCreateParams"]


class VerifiedContactCreateParams(TypedDict, total=False):
    phone_number: Required[str]
    """Contact phone number in E.164 format"""
