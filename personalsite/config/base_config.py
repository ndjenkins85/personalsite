import os
import urllib.parse

class BaseConfig(object):
    try:
        with open('latest_commit.txt', 'r', encoding="utf-16") as f:
           VERSION = (f.readlines()[0].split("\n")[0])
    except:
        VERSION = "Loaded locally"

    DOCKER_INTERNAL_URI = 'host.docker.internal'

    # File handling and azure file share
    print("Configured locally in verbose and debug mode")
    FILE_DB = "local" if os.environ.get('localfiles') else "azfs"

    AZ_FS_STORE = None
    AZ_FS_KEY = None
    AZ_FS_ACCOUNT = None

    DEBUG = True
    VERBOSE = True

    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'my_precious_two'

    # Evolved Analytics Site
    UPLOAD_FOLDER = None
    DROPZONE_MAX_FILE_SIZE = 50
    DROPZONE_INPUT_NAME = 'myfileinput'
    DROPZONE_MAX_FILES = 1
    DROPZONE_REDIRECT_VIEW = "dropzoneredirect"
    ALLOWED_EXTENSIONS = set(['csv', 'xlsx'])