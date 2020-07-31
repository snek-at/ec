import os
from app.config import Config


class DevConfig(Config):
    DEBUG = True

    RUN_SETTING = {"host": Config.HOST, "port": 5000, "debug": DEBUG}

    CONNECTOR_SETTINGS = {}

    # Secrets
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "XXXXXXXXXXXX")
    CONNECTOR_TOKEN = os.getenv("CONNECTOR_TOKEN", "XXXXXXXXXXXX")
