# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    token: str
    """Plaintext temporary bearer token. Store it securely; it is returned only once."""

    expires_at: datetime
    """ISO timestamp when the token expires."""

    phone_numbers: List[str]
    """Phone-number scope for this token. Empty means the token is account-scoped."""

    token_id: str
    """Token identifier used for revocation."""

    token_type: Literal["Bearer"]
