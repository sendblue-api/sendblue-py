# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageUpdateAppCardParams", "Layout"]


class MessageUpdateAppCardParams(TypedDict, total=False):
    fallback_text: str
    """Replacement fallback text for notifications and non-rendering surfaces."""

    idempotency_key: str
    """
    Reusing this key for the same App Card target returns the original update
    instead of sending again.
    """

    interactive: bool

    layout: Layout
    """Visible card fields mirroring Apple's MSMessageTemplateLayout."""

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
    """The iMessage expressive message style for this update."""

    url: str


class Layout(TypedDict, total=False):
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
