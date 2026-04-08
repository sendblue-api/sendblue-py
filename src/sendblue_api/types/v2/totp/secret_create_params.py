# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    algorithm: Literal["SHA1", "SHA256", "SHA512"]
    """Hash algorithm"""

    digits: Literal[6, 8]
    """Code length"""

    issuer: str
    """Service name (e.g. "GitHub", "Google")"""

    label: str
    """Human-readable label for this secret (e.g.

    "GitHub - agent@example.com"). Required unless `uri` is provided.
    """

    period: int
    """Rotation period in seconds"""

    secret: str
    """Base32-encoded TOTP secret. Omit to auto-generate one."""

    uri: str
    """Full `otpauth://totp/...` URI from a QR code.

    Overrides all other fields if provided.
    """
