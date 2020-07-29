import graphene

from app.api.schema.mutations.account import (
    AuthMutation,
    RefreshMutation,
)

from app.api.schema.mutations.page import PublishCompanyPageMutation


class Mutation(graphene.ObjectType):
    publish_company_page = PublishCompanyPageMutation.Field()

    auth = AuthMutation.Field()

    refresh = RefreshMutation.Field()
