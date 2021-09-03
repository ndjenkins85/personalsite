from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify

def create_app():
	app = Flask(__name__)
	app.config.from_object('personalsite.config.config.Config')
	return app

app = create_app()
CORS(app)
sslify = SSLify(app)

import personalsite.views

# Program version and changelog. __version__ is used in setup.py
# Poetry attaches to this version via poetry-version-plugin
# Git tagging is required in addition to these changes
# See CONTRIBUTING.md for more info

__version__ = "0.1.0" # Initial commit
