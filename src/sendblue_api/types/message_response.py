# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MessageResponse",
    "AppCard",
    "AppCardAppCard",
    "AppCardAppCardLayout",
    "AppCardInboundAppCard",
    "Location",
    "ReplyTo",
    "ThreadOriginator",
]


class AppCardAppCardLayout(BaseModel):
    """Visible card fields mirroring Apple's MSMessageTemplateLayout."""

    caption: Optional[str] = None

    image_subtitle: Optional[str] = FieldInfo(alias="imageSubtitle", default=None)
    """Secondary text overlaid on the preview image. Requires imageUrl."""

    image_title: Optional[str] = FieldInfo(alias="imageTitle", default=None)
    """Text overlaid on the preview image. Requires imageUrl."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """
    HTTPS preview image fetched by the worker and sent as a hidden card attachment.
    JPEG, PNG, HEIC, HEIF, and WebP are supported up to 10 MB.
    """

    subcaption: Optional[str] = None

    summary: Optional[str] = None
    """Fallback text used in notifications and non-rendering surfaces."""

    trailing_caption: Optional[str] = FieldInfo(alias="trailingCaption", default=None)

    trailing_subcaption: Optional[str] = FieldInfo(alias="trailingSubcaption", default=None)


class AppCardAppCard(BaseModel):
    """A Sendblue App Card rendered with Apple's Messages framework.

    App Cards require a V2 Mac line and an
    iMessage-capable recipient; they never fall back to SMS. The URL is delivered to the
    identified Messages extension when the recipient taps the card. An initial App Card may include
    `reply_to` to create an inline reply. Later state changes use the update endpoint, which sends a new
    Apple message in the same App Card session. The feature is unavailable on the free plan.
    """

    app_name: str = FieldInfo(alias="appName")

    extension_bundle_id: str = FieldInfo(alias="extensionBundleId")

    layout: AppCardAppCardLayout
    """Visible card fields mirroring Apple's MSMessageTemplateLayout."""

    team_id: str = FieldInfo(alias="teamId")

    url: str
    """URL delivered to the iMessage extension on tap.

    HTTPS URLs are limited to 2048 characters; data URLs carrying inline app state
    are limited to 16384.
    """

    app_store_id: Optional[int] = FieldInfo(alias="appStoreId", default=None)
    """Optional numeric App Store ID for recipients without the extension."""

    fallback_text: Optional[str] = FieldInfo(alias="fallbackText", default=None)
    """Fallback text for notifications and surfaces that cannot render the card."""

    interactive: Optional[bool] = None
    """
    Use Apple's live layout when the extension is installed; false always sends the
    static template layout.
    """

    session_identifier: Optional[str] = FieldInfo(alias="sessionIdentifier", default=None)
    """Optional caller-supplied App Card session UUID.

    Generated automatically when omitted.
    """

    update_message_handle: Optional[str] = FieldInfo(alias="updateMessageHandle", default=None)
    """
    Original message handle for an App Card continuation returned by the update
    endpoint.
    """


class AppCardInboundAppCard(BaseModel):
    """App Card session metadata received from an iMessage contact."""

    balloon_bundle_id: str = FieldInfo(alias="balloonBundleId")

    extension_bundle_id: str = FieldInfo(alias="extensionBundleId")

    revision: int
    """Retry-stable occurrence revision assigned to this inbound App Card state."""

    session_identifier: str = FieldInfo(alias="sessionIdentifier")

    team_id: str = FieldInfo(alias="teamId")

    url: str


AppCard: TypeAlias = Union[AppCardAppCard, AppCardInboundAppCard]


class Location(BaseModel):
    """Decoded Find My location share coordinates."""

    latitude: float

    longitude: float

    accuracy: Optional[float] = None
    """Horizontal accuracy in meters"""

    altitude: Optional[float] = None
    """Altitude in meters"""

    duration: Optional[str] = None
    """Share duration selected by the recipient"""

    timestamp: Optional[datetime] = None


class ReplyTo(BaseModel):
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same
    account, conversation, and sending line.
    """

    message_handle: str
    """Public handle of the immediate parent message"""

    part_index: Optional[int] = None
    """Advanced override for a known part of a multipart target.

    Omit this in normal reply requests and never guess it; requests default to 0.
    When replying to an attachment represented by its own webhook, use that
    webhook's `message_handle` and omit `part_index` so Sendblue can use the stored
    authoritative part. Responses omit it when no authoritative immediate-parent
    part is available.
    """


class ThreadOriginator(BaseModel):
    """Message that originated an iMessage inline-reply thread."""

    message_handle: str
    """Public handle of the thread's root message"""

    part: Optional[str] = None
    """Opaque Apple thread-originator part descriptor"""


class MessageResponse(BaseModel):
    account_email: Optional[str] = None
    """Email of the account that sent the message"""

    app_card: Optional[AppCard] = None
    """App Card data sent or received with this message."""

    content: Optional[str] = None
    """Message content"""

    date_created: Optional[datetime] = None
    """When the message was created"""

    date_updated: Optional[datetime] = None
    """When the message was last updated"""

    error_code: Optional[int] = None
    """Numeric error code if message failed"""

    error_message: Optional[str] = None
    """Error message if message failed"""

    from_number: Optional[str] = None
    """Sending phone number"""

    is_outbound: Optional[bool] = None
    """Whether this is an outbound message"""

    location: Optional[Location] = None
    """Decoded Find My location share coordinates."""

    media_url: Optional[str] = None
    """URL of attached media"""

    message_handle: Optional[str] = None
    """Unique identifier for tracking the message"""

    message_type: Optional[Literal["message", "group", "location"]] = None

    number: Optional[str] = None
    """Recipient phone number"""

    reply_to: Optional[ReplyTo] = None
    """Immediate parent of an iMessage inline reply.

    The target must belong to the same account, conversation, and sending line.
    """

    seat_id: Optional[str] = None
    """UUID of the seat that sent the message.

    Present when `seat_id` was provided on send, or for dashboard-originated group
    messages.
    """

    send_style: Optional[
        Literal[
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
    ] = None
    """The iMessage expressive message style"""

    sender_email: Optional[str] = None
    """Email of the seat (user) that sent the message.

    Auto-populated when a `seat_id` is provided on send. `null` for messages sent
    without a `seat_id`.
    """

    status: Optional[Literal["QUEUED", "SENT", "DELIVERED", "ERROR"]] = None

    thread_originator: Optional[ThreadOriginator] = None
    """Message that originated an iMessage inline-reply thread."""
