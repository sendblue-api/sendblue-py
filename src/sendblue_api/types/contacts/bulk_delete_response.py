# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BulkDeleteResponse"]


class BulkDeleteResponse(BaseModel):
    amount: Optional[int] = None
    """Number of contacts deleted"""

    status: Optional[str] = None
