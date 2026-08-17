# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VerificationListParams"]


class VerificationListParams(TypedDict, total=False):
    limit: int

    offset: int

    updated_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
