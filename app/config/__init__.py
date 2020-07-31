import os


class Config:
    GRAPHIQL = True
    DEBUG = False
    HOST = "0.0.0.0"

    SERVICE_NAME = "enterprise-connector"

    MONGODB_SETTINGS = {"db": SERVICE_NAME, "host": "mongomock://localhost"}

    RUN_SETTING = {"host": HOST, "port": 80, "debug": DEBUG}

    # Secrets
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", None)
    CONNECTOR_TOKEN = os.getenv("CONNECTOR_TOKEN", None)
