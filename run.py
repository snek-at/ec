import os

from app import create_app
from app.config.dev import Config, DevConfig

from app.gitlab import buildUser

if __name__ == "__main__":
    if not os.getenv("PRODUCTION", False):
        app = create_app(DevConfig)
    else:
        app = create_app(Config)

    app.run(**DevConfig.RUN_SETTING)
