# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageGetStatusParams"]


class MessageGetStatusParams(TypedDict, total=False):
    handle: Required[str]
    """The message handle of the message you want to check status for"""
