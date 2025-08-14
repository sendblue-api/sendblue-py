# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Contact"]


class Contact(BaseModel):
    assigned_to_email: Optional[str] = FieldInfo(alias="assignedToEmail", default=None)
    """Email of assigned user"""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Company name"""

    created_at: Optional[datetime] = None
    """When the contact was created"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """First name"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """Last name"""

    phone: Optional[str] = None
    """Phone number in E.164 format"""

    sendblue_number: Optional[str] = FieldInfo(alias="sendblueNumber", default=None)
    """Associated Sendblue phone number"""

    tags: Optional[List[str]] = None
    """Tags associated with the contact"""

    verified: Optional[bool] = None
    """Whether the contact is verified"""
