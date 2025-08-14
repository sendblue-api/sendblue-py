# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    number: Required[str]
    """Contact's phone number in E.164 format"""

    body_assigned_to_email_1: Annotated[str, PropertyInfo(alias="assigned_to_email")]
    """Email of assigned user"""

    body_assigned_to_email_2: Annotated[str, PropertyInfo(alias="assignedToEmail")]
    """Email of assigned user (alternative)"""

    body_first_name_1: Annotated[str, PropertyInfo(alias="first_name")]
    """Contact's first name"""

    body_first_name_2: Annotated[str, PropertyInfo(alias="firstName")]
    """Contact's first name (alternative)"""

    body_last_name_1: Annotated[str, PropertyInfo(alias="last_name")]
    """Contact's last name"""

    body_last_name_2: Annotated[str, PropertyInfo(alias="lastName")]
    """Contact's last name (alternative)"""

    body_phone_number_1: Annotated[str, PropertyInfo(alias="phone_number")]
    """Contact's phone number (alternative)"""

    body_phone_number_2: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Contact's phone number (alternative)"""

    body_sendblue_number_1: Annotated[str, PropertyInfo(alias="sendblue_number")]
    """Associated Sendblue phone number"""

    body_sendblue_number_2: Annotated[str, PropertyInfo(alias="sendblueNumber")]
    """Associated Sendblue phone number (alternative)"""

    tags: List[str]
    """Tags for the contact"""

    update_if_exists: bool
    """If true, updates the contact if it already exists"""
