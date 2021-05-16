from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Article, Category


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = '__all__'
        interfaces = (relay.Node, )

    def resolve_id(self, info):
        return super().resolve_id(info)


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = '__all__'
        interfaces = (relay.Node, )

    def resolve_id(self, info):
        return super().resolve_id(info)


class Query(ObjectType):
    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)

    category = relay.Node.Field(ArticleNode)
    all_categories = DjangoFilterConnectionField(ArticleNode)


class Mutation(ObjectType):
    pass


class Subscription(ObjectType):
    pass
