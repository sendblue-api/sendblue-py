# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GroupRenameParams"]


class GroupRenameParams(TypedDict, total=False):
    group_name: Required[Optional[str]]
    """
    New group name; whitespace-only values are rejected, while null or an empty
    string clears it
    """
