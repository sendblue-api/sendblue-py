# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupModifyParams"]


class GroupModifyParams(TypedDict, total=False):
    group_id: Required[str]
    """Group identifier"""

    modify_type: Required[Literal["add_recipient", "remove_recipient"]]
    """Type of modification to perform"""

    number: Required[str]
    """
    External participant to add or remove, in E.164 format (or an iMessage email
    address). Company-owned lines cannot be added or removed.
    """

    from_number: str
    """The Sendblue line to act from.

    It must belong to the account and already be a participant of the group. Free
    API accounts must provide it. Other accounts may omit it only when exactly one
    account line participates in the group. With no participating account line the
    request fails with `line_not_registered`; with multiple lines it fails with
    `ambiguous_sending_line`. No change is attempted in either case.
    """
