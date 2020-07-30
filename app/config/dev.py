import os
from app.config import Config


class DevConfig(Config):
    DEBUG = True

    RUN_SETTING = {"host": Config.HOST, "port": 5000, "debug": DEBUG}

    MONGODB_SETTINGS = {"db": Config.SERVICE_NAME, "host": "mongomock://localhost"}

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
