import graphene

from app.api.schema.unions.query import AccountUnion
from app.api.schema.queries.account import resolve_account


class Query(graphene.ObjectType):
    account = graphene.List(
        of_type=AccountUnion,
        token=graphene.NonNull(graphene.String),
        username=graphene.String(default_value=None),
        resolver=resolve_account,
    )
