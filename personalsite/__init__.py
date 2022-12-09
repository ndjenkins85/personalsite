# Copyright © 2023 by Nick Jenkins. All rights reserved

from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify


def create_app() -> Flask:
    """Creates the primary Flask app with config.

    Returns:
        Flask: returns flask app.
    """
    app = Flask(__name__)
    app.config.from_object("personalsite.config.config.Config")
    return app


app = create_app()
CORS(app)
sslify = SSLify(app)

import personalsite.views  # noqa: E402

# Program version and changelog. __version__ is used in setup.py
# Poetry attaches to this version via poetry-version-plugin
# Git tagging is required in addition to these changes
# See CONTRIBUTING.md for more info

__version__ = "0.2.1"  # Bugfix fix views not importing, nox problems, tags on article template
# "0.2.0"  # Nox tests passing
# "0.1.1"  # Add infrastructure tooling
# "0.1.0"  # Initial commit
