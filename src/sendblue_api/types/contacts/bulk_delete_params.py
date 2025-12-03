# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BulkDeleteParams"]


class BulkDeleteParams(TypedDict, total=False):
    contact_ids: Required[SequenceNotStr[str]]
    """Array of phone numbers in E.164 format to delete"""
