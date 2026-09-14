# Copyright © 2026 by Nick Jenkins. All rights reserved

"""Read optional identity asserted by the ndjenkins.com gateway."""

import os
from typing import Any, Dict, Optional

from flask import Flask, g, request
from jose import JWTError, jwt

EXPECTED_PREFIX = "/"
GATEWAY_AUTH_HEADER = "X-Gateway-Auth"
REQUIRED_CLAIMS = {"sub", "email", "name", "iat", "exp", "prefix"}


def _display_name(claims: Dict[str, Any]) -> str:
    """Choose a friendly identity label from trusted gateway claims."""
    name = claims.get("name")
    if isinstance(name, str) and name.strip():
        return name

    email = claims.get("email")
    if isinstance(email, str):
        local_part, separator, _ = email.strip().partition("@")
        if separator and local_part:
            return local_part
    return "there"


def gateway_identity(expected_prefix: str = EXPECTED_PREFIX) -> Optional[Dict[str, Any]]:
    """Verify the gateway token, treating every failure as anonymous.

    Args:
        expected_prefix: Exact gateway prefix this application serves.

    Returns:
        Verified identity claims, or None when no valid identity is present.
    """
    token = request.headers.get(GATEWAY_AUTH_HEADER, "")
    secret = os.getenv("GATEWAY_AUTH_SECRET", "")
    if not token or not secret:
        return None

    try:
        claims = jwt.decode(token, secret, algorithms=["HS256"])
    except JWTError:
        return None

    if claims.get("prefix") != expected_prefix or not REQUIRED_CLAIMS <= claims.keys():
        return None
    return {**claims, "display_name": _display_name(claims)}


def init_app(app: Flask) -> None:
    """Install optional gateway identity handling on a Flask application.

    Args:
        app: Flask application to configure.
    """

    @app.before_request
    def load_gateway_identity() -> None:
        """Expose verified claims for the current request."""
        g.identity = gateway_identity()

    @app.context_processor
    def gateway_identity_context() -> Dict[str, Optional[Dict[str, Any]]]:
        """Expose the optional identity to Jinja templates.

        Returns:
            The current request's verified identity.
        """
        return {"identity": getattr(g, "identity", None)}
