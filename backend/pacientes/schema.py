from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Paciente


class PacienteNode(DjangoObjectType):
    class Meta:
        model = Paciente
        filter_fields = {
            'nome_completo': ['exact', 'icontains', 'istartswith'],
            'user__email': ['exact', 'icontains']
        }
        interfaces = (relay.Node, )

    def resolve_id(self, info):
        return super().resolve_id(info)


class Query(ObjectType):
    paciente = relay.Node.Field(PacienteNode)
    all_pacientes = DjangoFilterConnectionField(PacienteNode)


class Mutation(ObjectType):
    pass


class Subscription(ObjectType):
    pass
