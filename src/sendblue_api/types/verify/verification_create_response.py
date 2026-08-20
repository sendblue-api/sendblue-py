# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .delivery_target import DeliveryTarget
from .hosted_verification import HostedVerification

__all__ = ["VerificationCreateResponse"]


class VerificationCreateResponse(BaseModel):
    account_sid: str

    channel: Literal["imessage"]

    date_created: datetime

    date_updated: datetime

    expires_at: datetime
    """ISO timestamp when the Verification expires."""

    service_sid: str

    sid: str

    status: Literal["pending", "approved", "expired", "canceled"]

    to: Optional[str] = None
    """
    Expected sender in E.164 format; older durable terminal records may return null.
    """

    url: str

    delivery_target: Optional[DeliveryTarget] = None
    """Present while the Verification is pending."""

    hosted: Optional[HostedVerification] = None
    """Present only when hosted options were supplied during creation."""
