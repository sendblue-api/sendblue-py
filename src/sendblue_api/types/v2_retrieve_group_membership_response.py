# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["V2RetrieveGroupMembershipResponse", "Data", "DataParticipant"]


class DataParticipant(BaseModel):
    contact_id: Optional[str] = None
    """Contact ID when this participant is linked to a contact"""

    handle: Optional[str] = None
    """
    Raw participant handle, usually an E.164 phone number but sometimes an iMessage
    email handle
    """

    name: Optional[str] = None
    """Contact or seat display name when available"""

    participant_id: Optional[str] = None
    """Unique participant row identifier"""

    phone: Optional[str] = None
    """
    Resolved participant phone number, preferring the stored group phone handle and
    falling back to contact phone. Email handles remain available in handle.
    """

    seat_id: Optional[str] = None
    """Seat ID when this participant is a team member"""

    type: Optional[Literal["contact", "seat"]] = None
    """Participant kind"""


class Data(BaseModel):
    created_at: Optional[datetime] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    latest_comm_at: Optional[datetime] = None

    latest_message_id: Optional[str] = None

    participant_numbers: Optional[List[str]] = None
    """Convenience list of resolved participant phone numbers.

    Participants with email-only handles remain in participants but are omitted
    here.
    """

    participants: Optional[List[DataParticipant]] = None

    updated_at: Optional[datetime] = None

    worker_group_id: Optional[str] = None
    """Worker-local iMessage group identifier when known"""


class V2RetrieveGroupMembershipResponse(BaseModel):
    data: Optional[Data] = None

    status: Optional[str] = None
