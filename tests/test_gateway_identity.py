# Copyright © 2026 by Nick Jenkins. All rights reserved

"""Gateway identity navigation and public legal page tests."""

import secrets
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

import pytest
from jose import jwt

from personalsite import app

TEST_SECRET = secrets.token_hex(32)
DEFAULT_TOKEN_LIFETIME = timedelta(minutes=5)


def _token(
    prefix: str = "/",
    expires_in: timedelta = DEFAULT_TOKEN_LIFETIME,
    name: str = "Nick",
    email: str = "nick@example.com",
) -> str:
    """Mint a representative gateway token for a test request.

    Args:
        prefix: Prefix claim placed in the token.
        expires_in: Time until the token expires.
        name: Name claim placed in the token.
        email: Email claim placed in the token.

    Returns:
        Encoded HS256 gateway token.
    """
    now = datetime.now(timezone.utc)
    claims: Dict[str, Any] = {
        "sub": "logto-user-123",
        "email": email,
        "name": name,
        "iat": int(now.timestamp()),
        "exp": int((now + expires_in).timestamp()),
        "prefix": prefix,
    }
    return jwt.encode(claims, TEST_SECRET, algorithm="HS256")


def _get(path: str = "/", token: Optional[str] = None) -> Any:  # NOQA: ANN401
    """Request a public page over the proxy's effective HTTPS scheme.

    Args:
        path: Site path to request.
        token: Optional gateway identity token.

    Returns:
        Flask test response.
    """
    headers = {"X-Forwarded-Proto": "https"}
    if token:
        headers["X-Gateway-Auth"] = token
    return app.test_client().get(path, headers=headers)


def test_anonymous_navigation(monkeypatch: pytest.MonkeyPatch) -> None:
    """Anonymous visitors see a sign-in link for their current path.

    Args:
        monkeypatch: Pytest environment patching fixture.
    """
    monkeypatch.setenv("GATEWAY_AUTH_SECRET", TEST_SECRET)

    response = _get("/privacy")

    assert response.status_code == 200
    assert b"Sign in</a>" in response.data
    assert b'href="/auth/login?rd=/privacy"' in response.data
    assert b"Sign out" not in response.data


@pytest.mark.parametrize(
    ("name", "email", "expected_display_name"),
    [
        ("Nick", "nick@example.com", "Nick"),
        ("", "bri.leo.nick.jenkins@gmail.com", "bri.leo.nick.jenkins"),
        ("", "", "there"),
    ],
    ids=["name", "email-local-part", "friendly-default"],
)
def test_signed_in_navigation_name_fallback(
    monkeypatch: pytest.MonkeyPatch,
    name: str,
    email: str,
    expected_display_name: str,
) -> None:
    """Signed-in navigation always displays a friendly account label.

    Args:
        monkeypatch: Pytest environment patching fixture.
        name: Gateway name claim under test.
        email: Gateway email claim under test.
        expected_display_name: Expected navigation label.
    """
    monkeypatch.setenv("GATEWAY_AUTH_SECRET", TEST_SECRET)

    response = _get(token=_token(name=name, email=email))

    assert response.status_code == 200
    assert f"Hi, {expected_display_name}".encode() in response.data
    assert b'href="/auth/logout?rd=/"' in response.data
    assert b"Sign in" not in response.data


@pytest.mark.parametrize(
    "token",
    [
        _token(prefix="/projects/personalsite"),
        _token(expires_in=timedelta(seconds=-1)),
        "not-a-jwt",
    ],
    ids=["wrong-prefix", "expired", "malformed"],
)
def test_invalid_gateway_identity_is_anonymous(monkeypatch: pytest.MonkeyPatch, token: str) -> None:
    """Invalid identity never prevents access to a public page.

    Args:
        monkeypatch: Pytest environment patching fixture.
        token: Invalid gateway token under test.
    """
    monkeypatch.setenv("GATEWAY_AUTH_SECRET", TEST_SECRET)

    response = _get(token=token)

    assert response.status_code == 200
    assert b"Sign in" in response.data
    assert b"Hi, Nick" not in response.data


@pytest.mark.parametrize("path", ["/privacy", "/terms"])
def test_legal_pages_are_public(path: str) -> None:
    """Required legal pages render publicly.

    Args:
        path: Legal page route under test.
    """
    response = _get(path)

    assert response.status_code == 200
    assert b"nick_jenkins@outlook.com" in response.data


def test_personalsite_session_cookie_is_isolated() -> None:
    """The site's Flask cookie cannot collide with other path-prefixed apps."""
    assert app.config["SESSION_COOKIE_NAME"] == "personalsite_session"
    assert app.config["SESSION_COOKIE_SECURE"] is True
    assert app.config["SESSION_COOKIE_SAMESITE"] == "Lax"
