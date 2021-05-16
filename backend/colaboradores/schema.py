from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Colaborador


class ColaboradorNode(DjangoObjectType):
    class Meta:
        model = Colaborador
        filter_fields = '__all__'
        interfaces = (relay.Node, )

    def resolve_id(self, info):
        return super().resolve_id(info)


class Query(ObjectType):
    colaborador = relay.Node.Field(ColaboradorNode)
    all_colaboradores = DjangoFilterConnectionField(ColaboradorNode)


class Mutation(ObjectType):
    pass


class Subscription(ObjectType):
    pass
