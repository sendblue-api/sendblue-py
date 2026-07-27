# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SendCarouselSendParams", "ReplyTo"]


class SendCarouselSendParams(TypedDict, total=False):
    from_number: Required[str]
    """Your Sendblue phone number in E.164 format (must be a V2/Mac Mini line)"""

    media_urls: Required[SequenceNotStr[str]]
    """Array of HTTPS image URLs to send as a carousel (2-20 items)"""

    number: Required[str]
    """Recipient phone number in E.164 format"""

    metadata: object
    """Additional metadata to attach to the message"""

    reply_to: ReplyTo
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same account, conversation, and sending line.
    """

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


class ReplyTo(TypedDict, total=False):
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same
    account, conversation, and sending line.
    """

    message_handle: Required[str]
    """Public handle of the immediate parent message"""

    part_index: int
    """Advanced override for a known part of a multipart target.

    Omit this in normal reply requests and never guess it; requests default to 0.
    When replying to an attachment represented by its own webhook, use that
    webhook's `message_handle` and omit `part_index` so Sendblue can use the stored
    authoritative part. Responses omit it when no authoritative immediate-parent
    part is available.
    """
