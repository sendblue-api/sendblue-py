# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..contact import Contact
from ..._models import BaseModel

__all__ = ["BulkCreateResponse"]


class BulkCreateResponse(BaseModel):
    contacts: Optional[List[Contact]] = None

    status: Optional[str] = None
