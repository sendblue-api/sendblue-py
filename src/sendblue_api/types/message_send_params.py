# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    content: Required[str]
    """Message text content"""

    from_number: Required[str]
    """**REQUIRED** - The phone number to send from.

    Must be one of your registered Sendblue phone numbers in E.164 format. Without
    this parameter, the message will fail to send.
    """

    number: Required[str]
    """Recipient phone number in E.164 format"""

    media_url: str
    """URL of media file to send (images, videos, etc.)"""

    seat_id: str
    """Optional.

    Identifies the seat (user) sending the message so the message is attributed to a
    specific rep. Accepts either the seat UUID or the Firebase Auth subject. When
    provided, `sender_email` is auto-populated on the message record and webhook
    payloads. Returns 400 if the seat is not found.
    """

    send_style: Literal[
        "celebration",
        "shooting_star",
        "fireworks",
        "lasers",
        "love",
        "confetti",
        "balloons",
        "spotlight",
        "echo",
        "invisible",
        "gentle",
        "loud",
        "slam",
    ]
    """The iMessage expressive message style"""

    status_callback: str
    """Webhook URL for message status updates"""
