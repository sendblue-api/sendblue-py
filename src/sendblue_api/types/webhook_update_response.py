# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .webhook_configuration import WebhookConfiguration

__all__ = ["WebhookUpdateResponse"]


class WebhookUpdateResponse(BaseModel):
    status: Literal["OK", "ERROR"]

    message: Optional[str] = None

    webhooks: Optional[WebhookConfiguration] = None
    """Updated webhook configration (partial)"""
