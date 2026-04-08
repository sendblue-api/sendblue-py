# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TotpGetCodeResponse"]


class TotpGetCodeResponse(BaseModel):
    code: Optional[str] = None
    """The current TOTP code"""

    expires_in: Optional[int] = None
    """Seconds until this code rotates"""

    status: Optional[str] = None
