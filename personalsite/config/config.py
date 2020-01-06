class Config():
    DOCKER_INTERNAL_URI = 'host.docker.internal'

    DEBUG = True
    VERBOSE = True

    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'my_precious_two'

    SITEMAP_EXCLUDES = ["dropzoneredirect", "login", "logout", "version"]
    SITEURL = "https://www.nickjenkins.com.au"