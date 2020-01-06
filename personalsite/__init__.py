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
