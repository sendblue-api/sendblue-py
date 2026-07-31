# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendParams", "AppCard", "AppCardLayout", "ReplyTo"]


class MessageSendParams(TypedDict, total=False):
    from_number: Required[str]
    """**REQUIRED** - The phone number to send from.

    Must be one of your registered Sendblue phone numbers in E.164 format. Without
    this parameter, the message will fail to send.
    """

    number: Required[str]
    """Recipient phone number in E.164 format"""

    app_card: AppCard
    """A Sendblue App Card rendered with Apple's Messages framework.

    App Cards require a V2 Mac line and an iMessage-capable recipient; they never
    fall back to SMS. The URL is delivered to the identified Messages extension when
    the recipient taps the card. An initial App Card may include `reply_to` to
    create an inline reply. Later state changes use the update endpoint, which sends
    a new Apple message in the same App Card session. The feature is unavailable on
    the free plan.
    """

    content: str
    """Message text content. Optional when `media_url` or `app_card` is provided."""

    media_url: str
    """URL of media file to send (images, videos, etc.)"""

    reply_to: ReplyTo
    """Optional inline-reply target.

    This may be combined with `app_card`; the resulting App Card is sent as an
    inline reply to the target.
    """

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


class AppCardLayout(TypedDict, total=False):
    """Visible card fields mirroring Apple's MSMessageTemplateLayout."""

    caption: str

    image_subtitle: Annotated[str, PropertyInfo(alias="imageSubtitle")]
    """Secondary text overlaid on the preview image. Requires imageUrl."""

    image_title: Annotated[str, PropertyInfo(alias="imageTitle")]
    """Text overlaid on the preview image. Requires imageUrl."""

    image_url: Annotated[str, PropertyInfo(alias="imageUrl")]
    """
    HTTPS preview image fetched by the worker and sent as a hidden card attachment.
    JPEG, PNG, HEIC, HEIF, and WebP are supported up to 10 MB.
    """

    subcaption: str

    summary: str
    """Fallback text used in notifications and non-rendering surfaces."""

    trailing_caption: Annotated[str, PropertyInfo(alias="trailingCaption")]

    trailing_subcaption: Annotated[str, PropertyInfo(alias="trailingSubcaption")]


class AppCard(TypedDict, total=False):
    """A Sendblue App Card rendered with Apple's Messages framework.

    App Cards require a V2 Mac line and an
    iMessage-capable recipient; they never fall back to SMS. The URL is delivered to the
    identified Messages extension when the recipient taps the card. An initial App Card may include
    `reply_to` to create an inline reply. Later state changes use the update endpoint, which sends a new
    Apple message in the same App Card session. The feature is unavailable on the free plan.
    """

    app_name: Required[Annotated[str, PropertyInfo(alias="appName")]]

    extension_bundle_id: Required[Annotated[str, PropertyInfo(alias="extensionBundleId")]]

    layout: Required[AppCardLayout]
    """Visible card fields mirroring Apple's MSMessageTemplateLayout."""

    team_id: Required[Annotated[str, PropertyInfo(alias="teamId")]]

    url: Required[str]
    """URL delivered to the iMessage extension on tap.

    HTTPS URLs are limited to 2048 characters; data URLs carrying inline app state
    are limited to 16384.
    """

    app_store_id: Annotated[int, PropertyInfo(alias="appStoreId")]
    """Optional numeric App Store ID for recipients without the extension."""

    fallback_text: Annotated[str, PropertyInfo(alias="fallbackText")]
    """Fallback text for notifications and surfaces that cannot render the card."""

    interactive: bool
    """
    Use Apple's live layout when the extension is installed; false always sends the
    static template layout.
    """

    session_identifier: Annotated[str, PropertyInfo(alias="sessionIdentifier")]
    """Optional caller-supplied App Card session UUID.

    Generated automatically when omitted.
    """


class ReplyTo(TypedDict, total=False):
    """Optional inline-reply target.

    This may be combined with `app_card`;
    the resulting App Card is sent as an inline reply to the target.
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
