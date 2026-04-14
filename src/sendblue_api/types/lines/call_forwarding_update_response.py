# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallForwardingUpdateResponse"]


class CallForwardingUpdateResponse(BaseModel):
    forwarding_number: Optional[str] = None
    """The number calls are forwarded to, or null if not set"""

    sendblue_number: str
    """The Sendblue phone number (E.164)"""
