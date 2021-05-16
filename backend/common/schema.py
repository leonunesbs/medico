import graphene

import users.schema
import blog.schema
import colaboradores.schema
import pacientes.schema


class Query(
    users.schema.Query,
    blog.schema.Query,
    colaboradores.schema.Query,
    pacientes.schema.Query,
    graphene.ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
    users.schema.Mutation,
    blog.schema.Mutation,
    colaboradores.schema.Mutation,
    pacientes.schema.Mutation, graphene.ObjectType
):
    pass


class Subscription(
    users.schema.Subscription,
    blog.schema.Subscription,
    colaboradores.schema.Subscription,
    pacientes.schema.Subscription,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query)
