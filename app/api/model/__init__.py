from mongoengine import connect


from app.api.model.account import AccountModel


class Mongo:
    def __init__(self, app):
        settings = app.config["MONGODB_SETTINGS"]

        connect(**settings)

        print("[INFO] MongoEngine initialized with {}".format(settings))
