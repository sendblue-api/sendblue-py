# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Contact"]


class Contact(BaseModel):
    assigned_to_email: Optional[str] = None
    """Email of assigned user"""

    company_name: Optional[str] = None
    """Company name"""

    created_at: Optional[datetime] = None
    """When the contact was created"""

    first_name: Optional[str] = None
    """First name"""

    last_name: Optional[str] = None
    """Last name"""

    phone: Optional[str] = None
    """Phone number in E.164 format"""

    sendblue_number: Optional[str] = None
    """Associated Sendblue phone number"""

    tags: Optional[List[str]] = None
    """Tags associated with the contact"""

    verified: Optional[bool] = None
    """Whether the contact is verified"""
