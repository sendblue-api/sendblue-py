# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GroupRenameParams"]


class GroupRenameParams(TypedDict, total=False):
    name: Required[Optional[str]]
    """New group name, or null/empty string to clear it"""
