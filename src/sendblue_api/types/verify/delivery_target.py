# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DeliveryTarget"]


class DeliveryTarget(BaseModel):
    code: str
    """Code the expected sender must text to `pool_number`."""

    pool_number: str
    """Sendblue phone number that should receive the verification code."""

    sms_deep_link: str
    """Messages/SMS deep link with the destination and code prefilled."""
