import graphene
import os
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from app.api.schema.unions.mutation import ResponseUnion
from app.api.schema.fields import ResponseMessageField


class PublishCompanyPageMutation(graphene.Mutation):
    class Arguments(object):
        token = graphene.String()
        page = graphene.JSONString()

    result = graphene.Field(ResponseUnion)

    @classmethod
    def mutate(cls, _, info, token, page):
        print(token, page)

        if token == os.getenv("CONNECTOR_TOKEN", None):
            # Select your transport with a defined url endpoint

            transport = RequestsHTTPTransport(
                url="https://engine.snek.at/api/graphiql",
                use_json=True,
                headers={
                    "Content-type": "application/json",
                    # "Authorization": "token"
                },
                verify=False,
                retries=3,
            )

            client = Client(transport=transport, fetch_schema_from_transport=True,)

            query = gql(
                """
                query{
                format
                }
            """
            )

            client.execute(query)

            return PublishCompanyPageMutation(
                ResponseMessageField(
                    is_success=True, message="Page successfully pushed"
                )
            )

        return PublishCompanyPageMutation(
            ResponseMessageField(is_success=False, message="Something went wrong")
        )
