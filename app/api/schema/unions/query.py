from app.api.schema.fields import ResponseMessageField, AccountField

from flask_graphql_auth import AuthInfoField
import graphene


class AccountUnion(graphene.Union):
    class Meta:
        types = (AccountField, ResponseMessageField, AuthInfoField)
