from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User


# Graphene will automatically map the User model's fields onto the UserNode.
# This is configured in the UserNode's Meta class (as you can see below)
class UsersNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['email', 'is_staff']
        interfaces = (relay.Node, )

    def resolve_id(self, info):
        return super().resolve_id(info)


class Query(ObjectType):
    users = relay.Node.Field(UsersNode)
    all_users = DjangoFilterConnectionField(UsersNode)
