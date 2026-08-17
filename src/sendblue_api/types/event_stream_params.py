# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EventStreamParams"]


class EventStreamParams(TypedDict, total=False):
    types: str
    """Optional comma-separated allowlist of event types"""
