# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SecretCreateResponse", "TotpSecret"]


class TotpSecret(BaseModel):
    id: Optional[str] = None
    """Unique identifier for this TOTP secret"""

    algorithm: Optional[Literal["SHA1", "SHA256", "SHA512"]] = None
    """Hash algorithm used"""

    created_at: Optional[datetime] = None

    digits: Optional[int] = None
    """Code length (6 or 8)"""

    issuer: Optional[str] = None
    """Service name"""

    label: Optional[str] = None
    """Human-readable label"""

    period: Optional[int] = None
    """Rotation period in seconds"""

    secret: Optional[str] = None
    """Base32 secret — only returned on creation, never on list/get"""


class SecretCreateResponse(BaseModel):
    status: Optional[str] = None

    totp_secret: Optional[TotpSecret] = None
