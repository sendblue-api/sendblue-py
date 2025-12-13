# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    account_email: str
    """Filter by account email"""

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter messages created after this date (ISO 8601 format)"""

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter messages created before this date (ISO 8601 format)"""

    from_number: str
    """Filter by sender phone number"""

    group_id: str
    """Filter by group ID"""

    is_outbound: Literal["true", "false"]
    """Filter by message direction"""

    limit: int
    """Maximum number of messages to return"""

    message_type: Literal["message", "group"]
    """Filter by message type"""

    number: str
    """Filter by any phone number (from or to)"""

    offset: int
    """Number of messages to skip"""

    order_by: Literal["createdAt", "updatedAt", "sentAt"]
    """Field to order messages by"""

    order_direction: Literal["asc", "desc"]
    """Sort order"""

    sendblue_number: str
    """Filter by Sendblue phone number"""

    sent_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter messages sent after this date (ISO 8601 format)"""

    sent_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter messages sent before this date (ISO 8601 format)"""

    service: Literal["iMessage", "SMS"]
    """Filter by service type"""

    status: Literal[
        "REGISTERED", "PENDING", "SENT", "DELIVERED", "RECEIVED", "QUEUED", "ERROR", "DECLINED", "ACCEPTED", "SUCCESS"
    ]
    """Filter by message status"""

    to_number: str
    """Filter by recipient phone number"""

    updated_at_gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter messages updated after this date (ISO 8601 format)"""

    updated_at_lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter messages updated before this date (ISO 8601 format)"""

    worker_id: str
    """Filter by worker ID (Admin only)"""
