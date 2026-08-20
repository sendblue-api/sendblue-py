# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["HostedVerification"]


class HostedVerification(BaseModel):
    component_script: str
    """Web-component script URL. Load this value exactly as returned."""

    expires_at: datetime
    """ISO timestamp when the Verification expires."""

    session_id: str
    """Hosted widget session identifier."""

    url: str
    """Origin-bound widget URL containing a one-session bearer token in its fragment.

    Do not log, persist, or move the token into a query parameter.
    """
