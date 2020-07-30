from flask import Flask
from flask_graphql_auth import GraphQLAuth
from app.api import API


def create_app(*config_cls):
    app = Flask(__name__)

    for config in config_cls:
        app.config.from_object(config)

    print(
        "[INFO] Flask application initialized with {0}".format(
            [config.__name__ for config in config_cls]
        )
    )

    API(app)
    GraphQLAuth(app)

    return app
