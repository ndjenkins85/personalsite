# Copyright © 2023 by Nick Jenkins. All rights reserved

from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app() -> Flask:
    """Creates the primary Flask app with config.

    Returns:
        Flask: returns flask app.
    """
    app = Flask(__name__)
    app.config.from_object("personalsite.config.config.Config")
    return app


app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)  # type: ignore[method-assign]
CORS(app, origins=["https://www.ndjenkins.com", "https://ndjenkins.com"])
sslify = SSLify(app)

from personalsite.gateway_identity import init_app as init_gateway_identity  # noqa: E402

init_gateway_identity(app)

import personalsite.views  # noqa: E402

# Program version and changelog. __version__ is used in setup.py
# Poetry attaches to this version via poetry-version-plugin
# Git tagging is required in addition to these changes
# See CONTRIBUTING.md for more info

__version__ = "0.2.1"  # Bugfix fix views not importing, nox problems, tags on article template
# "0.2.0"  # Nox tests passing
# "0.1.1"  # Add infrastructure tooling
# "0.1.0"  # Initial commit
