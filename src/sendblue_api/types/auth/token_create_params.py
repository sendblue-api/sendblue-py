# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["TokenCreateParams"]


class TokenCreateParams(TypedDict, total=False):
    expires_in_seconds: int
    """Token lifetime in seconds. Defaults to 900 seconds when omitted."""

    phone_number: str
    """Single Sendblue phone number to scope the token to.

    Cannot be combined with `phone_numbers`.
    """

    phone_numbers: SequenceNotStr[str]
    """Sendblue phone numbers to scope the token to.

    Cannot be combined with `phone_number`.
    """
