import graphene

from app.api.schema.fields.account import AccountField
from app.api.schema.fields.comment import CommentField


class PostField(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    text = graphene.String()
    upload_on = graphene.DateTime()
    comment = graphene.List(of_type=CommentField)
    author = graphene.Field(AccountField)
