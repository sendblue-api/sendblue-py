# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    number: Required[str]
    """Contact's phone number in E.164 format (preferred)"""

    body_assigned_to_email_1: Annotated[str, PropertyInfo(alias="assigned_to_email")]
    """Email of assigned user (preferred)"""

    body_assigned_to_email_2: Annotated[str, PropertyInfo(alias="assignedToEmail")]
    """Email of assigned user (deprecated, use assigned_to_email)"""

    body_first_name_1: Annotated[str, PropertyInfo(alias="first_name")]
    """Contact's first name (preferred)"""

    body_first_name_2: Annotated[str, PropertyInfo(alias="firstName")]
    """Contact's first name (deprecated, use first_name)"""

    body_last_name_1: Annotated[str, PropertyInfo(alias="last_name")]
    """Contact's last name (preferred)"""

    body_last_name_2: Annotated[str, PropertyInfo(alias="lastName")]
    """Contact's last name (deprecated, use last_name)"""

    body_phone_number_1: Annotated[str, PropertyInfo(alias="phone_number")]
    """Contact's phone number (deprecated, use number)"""

    body_phone_number_2: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Contact's phone number (deprecated, use number)"""

    body_sendblue_number_1: Annotated[str, PropertyInfo(alias="sendblue_number")]
    """Associated Sendblue phone number to send with (preferred)"""

    body_sendblue_number_2: Annotated[str, PropertyInfo(alias="sendblueNumber")]
    """Associated Sendblue phone number (deprecated, use sendblue_number)"""

    tags: SequenceNotStr[str]
    """Tags for the contact"""

    update_if_exists: bool
    """If true, updates the contact if it already exists"""
