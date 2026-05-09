# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SendCarouselSendParams"]


class SendCarouselSendParams(TypedDict, total=False):
    from_number: Required[str]
    """Your Sendblue phone number in E.164 format (must be a V2/Mac Mini line)"""

    media_urls: Required[SequenceNotStr[str]]
    """Array of HTTPS image URLs to send as a carousel (2-20 items)"""

    number: Required[str]
    """Recipient phone number in E.164 format"""

    metadata: object
    """Additional metadata to attach to the message"""

    seat_id: str
    """Optional.

    Identifies the seat (user) sending the carousel so it is attributed to a
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
