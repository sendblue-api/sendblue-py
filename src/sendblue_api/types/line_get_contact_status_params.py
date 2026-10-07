# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LineGetContactStatusParams"]


class LineGetContactStatusParams(TypedDict, total=False):
    number: Required[str]
    """Contact phone number (E.164 format).

    Formatted phone numbers are converted to E.164; email addresses are not
    supported.
    """

    sendblue_number: Required[str]
    """Your Sendblue phone number (E.164 format).

    Old lines still available during a replacement grace period are also supported.
    """
