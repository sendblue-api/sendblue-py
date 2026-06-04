# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TypingIndicatorSendParams"]


class TypingIndicatorSendParams(TypedDict, total=False):
    from_number: Required[str]
    """
    The Sendblue phone number you want to send the typing indicator from (E.164
    format). This should be the number you use to send messages.
    """

    number: Required[str]
    """The number you want to send a typing indicator to (E.164 format)"""

    max_duration_ms: int
    """Optional maximum duration for a start indicator, in milliseconds."""

    state: Literal["start", "stop"]
    """Optional typing state. Defaults to a start indicator when omitted."""
