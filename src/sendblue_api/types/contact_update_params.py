# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    assigned_to_email: Annotated[str, PropertyInfo(alias="assignedToEmail")]

    company_name: Annotated[str, PropertyInfo(alias="companyName")]

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    sendblue_number: Annotated[str, PropertyInfo(alias="sendblueNumber")]

    tags: List[str]
