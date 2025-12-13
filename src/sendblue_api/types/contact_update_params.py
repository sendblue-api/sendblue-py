# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    body_assigned_to_email_1: Annotated[str, PropertyInfo(alias="assigned_to_email")]
    """Email of assigned user (preferred)"""

    body_assigned_to_email_2: Annotated[str, PropertyInfo(alias="assignedToEmail")]
    """Deprecated, use assigned_to_email"""

    body_company_name_1: Annotated[str, PropertyInfo(alias="company_name")]
    """Company name (preferred)"""

    body_company_name_2: Annotated[str, PropertyInfo(alias="companyName")]
    """Deprecated, use company_name"""

    body_first_name_1: Annotated[str, PropertyInfo(alias="first_name")]
    """Contact's first name (preferred)"""

    body_first_name_2: Annotated[str, PropertyInfo(alias="firstName")]
    """Deprecated, use first_name"""

    body_last_name_1: Annotated[str, PropertyInfo(alias="last_name")]
    """Contact's last name (preferred)"""

    body_last_name_2: Annotated[str, PropertyInfo(alias="lastName")]
    """Deprecated, use last_name"""

    body_sendblue_number_1: Annotated[str, PropertyInfo(alias="sendblue_number")]
    """Associated Sendblue phone number (preferred)"""

    body_sendblue_number_2: Annotated[str, PropertyInfo(alias="sendblueNumber")]
    """Deprecated, use sendblue_number"""

    tags: SequenceNotStr[str]
