# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TypingIndicatorSendParams"]


class TypingIndicatorSendParams(TypedDict, total=False):
    from_number: Required[str]
    """
    The Sendblue phone number you want to send the typing indicator from (E.164
    format). This should be the number you use to send messages.
    """

    number: Required[str]
    """The number you want to send a typing indicator to (E.164 format)"""
