# Copyright © 2025 by Nick Jenkins. All rights reserved

"""Application security behavior tests."""

from typing import Optional

import pytest

from personalsite import app
from personalsite.config import config


@pytest.mark.parametrize("route", ["/resume/dynamic", "/cover/dynamic"])
@pytest.mark.parametrize("path", ["nested/name", "..", "name.txt", "name%20with%20spaces"])
def test_dynamic_document_routes_reject_unsafe_paths(route: str, path: str) -> None:
    """Private document routes reject traversal and unexpected identifiers.

    Args:
        route: Dynamic document route under test.
        path: Unsafe path fragment to request.
    """
    response = app.test_client().get(f"{route}/{path}", headers={"X-Forwarded-Proto": "https"})
    assert response.status_code == 404


def test_proxy_headers_prevent_https_redirect() -> None:
    """SSL enforcement trusts the single terminating reverse proxy."""
    response = app.test_client().get(
        "/",
        headers={
            "Host": "railway.internal",
            "X-Forwarded-Host": "www.ndjenkins.com",
            "X-Forwarded-Proto": "https",
        },
    )
    assert response.status_code == 200


@pytest.mark.parametrize(
    ("origin", "allowed"),
    [
        ("https://www.ndjenkins.com", True),
        ("https://ndjenkins.com", True),
        ("https://example.com", False),
    ],
)
def test_cors_allowlist(origin: str, allowed: bool) -> None:
    """Only the production site origins receive CORS permission.

    Args:
        origin: Request origin to test.
        allowed: Whether the origin should receive a CORS header.
    """
    response = app.test_client().get("/", headers={"Origin": origin, "X-Forwarded-Proto": "https"})
    assert (response.headers.get("Access-Control-Allow-Origin") == origin) is allowed


def test_secret_key_fallback_is_random(monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture) -> None:
    """An unset key gets a noisy, per-call random fallback.

    Args:
        monkeypatch: Pytest environment patching fixture.
        caplog: Pytest log capture fixture.
    """
    monkeypatch.delenv("SECRET_KEY", raising=False)
    with caplog.at_level("WARNING"):
        first_key = config._get_secret_key()
        second_key = config._get_secret_key()

    assert first_key != second_key
    assert "SECRET_KEY IS UNSET" in caplog.text


@pytest.mark.parametrize(("value", "expected"), [(None, False), ("false", False), ("true", True), ("1", True)])
def test_debug_is_environment_controlled(monkeypatch: pytest.MonkeyPatch, value: Optional[str], expected: bool) -> None:
    """Debug mode defaults off and recognizes explicit true values.

    Args:
        monkeypatch: Pytest environment patching fixture.
        value: Environment value to parse, or None when unset.
        expected: Expected debug-mode result.
    """
    if value is None:
        monkeypatch.delenv("FLASK_DEBUG", raising=False)
    else:
        monkeypatch.setenv("FLASK_DEBUG", value)

    assert config._get_debug() is expected
