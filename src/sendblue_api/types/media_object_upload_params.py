# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MediaObjectUploadParams"]


class MediaObjectUploadParams(TypedDict, total=False):
    media_url: Required[str]
    """URL of the media file to upload"""
