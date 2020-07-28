import graphene

from app.api.schema.fields import AccountField


class CommentField(graphene.ObjectType):
    text = graphene.String()
    author = graphene.Field(type=AccountField)
