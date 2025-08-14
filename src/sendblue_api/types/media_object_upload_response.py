# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MediaObjectUploadResponse"]


class MediaObjectUploadResponse(BaseModel):
    media_object_id: Optional[str] = FieldInfo(alias="mediaObjectId", default=None)

    message: Optional[str] = None

    status: Optional[str] = None
