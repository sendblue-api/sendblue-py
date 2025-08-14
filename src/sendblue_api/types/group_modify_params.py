# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupModifyParams"]


class GroupModifyParams(TypedDict, total=False):
    group_id: Required[str]
    """Group identifier"""

    modify_type: Required[Literal["add_recipient"]]
    """Type of modification to perform"""

    number: Required[str]
    """Phone number to add/modify in E.164 format"""
