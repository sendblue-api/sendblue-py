# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams", "Hosted"]


class VerificationCreateParams(TypedDict, total=False):
    to: Required[str]
    """E.164 phone number that must send the verification message."""

    hosted: Hosted
    """Options for an origin-bound Hosted Verify widget session.

    Nested keys are strict snake_case. `parent_origin` must be an exact HTTPS origin
    with a DNS hostname. `127.0.0.1` is also accepted, and HTTP is allowed only for
    `localhost` or `127.0.0.1` development origins. Wildcards and other IP literals
    are rejected because browsers cannot enforce them as exact CSP `frame-ancestors`
    sources.
    """


class Hosted(TypedDict, total=False):
    """Options for an origin-bound Hosted Verify widget session.

    Nested keys are strict snake_case.
    `parent_origin` must be an exact HTTPS origin with a DNS hostname. `127.0.0.1` is also accepted,
    and HTTP is allowed only for `localhost` or `127.0.0.1` development origins. Wildcards and other
    IP literals are rejected because browsers cannot enforce them as exact CSP `frame-ancestors` sources.
    """

    parent_origin: Required[str]
    """
    Exact website origin allowed to embed the widget, with no path, query, or
    fragment.
    """

    accent_color: str
    """Six-digit hexadecimal accent color."""

    brand_name: str
    """Brand name displayed by the widget. Defaults to Sendblue."""

    theme: Literal["light", "dark", "auto"]
