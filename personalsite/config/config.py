"""Configurations for use across personal project."""

# Copyright © 2023 by Nick Jenkins. All rights reserved


class Config:
    """Config used in Flask and docker."""

    DOCKER_INTERNAL_URI = "host.docker.internal"

    DEBUG = True
    VERBOSE = True

    SECRET_KEY = "my_precious"  # pragma: noqa
    SECURITY_PASSWORD_SALT = "my_precious_two"  # pragma: noqa

    SITEMAP_EXCLUDES = ["dropzoneredirect", "login", "logout", "version"]
    SITEURL = "https://www.ndjenkins.com"
