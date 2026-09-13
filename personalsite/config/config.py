"""Configurations for use across personal project."""

# Copyright © 2023 by Nick Jenkins. All rights reserved

import logging
import os
import secrets

logger = logging.getLogger(__name__)


def _get_secret_key() -> str:
    """Load the session signing key, with a safe development fallback.

    Returns:
        A configured or random session signing key.
    """
    secret_key = os.getenv("SECRET_KEY")
    if secret_key:
        return secret_key

    logger.warning(
        "SECRET_KEY IS UNSET: using a random per-process value; sessions will not "
        "survive restarts or work across processes. Set SECRET_KEY in the environment."
    )
    return secrets.token_urlsafe(32)


def _get_debug() -> bool:
    """Read Flask debug mode from the environment, defaulting to disabled.

    Returns:
        Whether Flask debug mode is explicitly enabled.
    """
    return os.getenv("FLASK_DEBUG", "false").strip().lower() in {"1", "true", "yes", "on"}


class Config:
    """Config used in Flask and docker."""

    DOCKER_INTERNAL_URI = "host.docker.internal"

    DEBUG = _get_debug()
    VERBOSE = True

    SECRET_KEY = _get_secret_key()
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")

    SITEMAP_EXCLUDES = ["dropzoneredirect", "login", "logout", "version"]
    SITEURL = "https://www.ndjenkins.com"
