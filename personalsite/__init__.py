from flask import Flask
from flask_cors import CORS
from flask_sslify import SSLify
from azure.storage.file import FileService

def create_app():
	app = Flask(__name__)
	app.config.from_object('personalsite.config.base_config.BaseConfig')

	# db.init_app(app)
	db = None

	# from evolvedanalytics.media.views import media
	# app.register_blueprint(media)

	return app, db

app = Flask(__name__)

app, db = create_app()
CORS(app)
sslify = SSLify(app)

#file_service = FileService(account_name=app.config["AZ_FS_ACCOUNT"], account_key=app.config["AZ_FS_KEY"])
file_service = None

import personalsite.views
