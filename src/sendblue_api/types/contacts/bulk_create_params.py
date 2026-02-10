# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BulkCreateParams", "Contact"]


class BulkCreateParams(TypedDict, total=False):
    contacts: Required[Iterable[Contact]]


class Contact(TypedDict, total=False):
    phone: Required[str]
    """Phone number in E.164 format"""

    company_name: str
    """Company name"""

    custom_variables: Dict[str, str]
    """Custom key-value pairs.

    Keys are human-readable labels; new labels are auto-created.
    """

    first_name: str
    """Contact's first name"""

    last_name: str
    """Contact's last name"""

    tags: SequenceNotStr[str]
