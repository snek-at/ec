from flask import Flask
from app.api.schema import Schema
from app.api.model import Mongo


class API:
    def __init__(self, app):
        Mongo(app)
        Schema(app)
