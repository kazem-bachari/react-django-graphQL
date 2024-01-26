import graphene
from graphene_django import DjangoObjectType

from .models import Book, Categorize


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "category")


class CategorizeType(DjangoObjectType):
    class Meta:
        model = Categorize
        fields = ("id", "title")


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    categorizes = graphene.List(CategorizeType)
    # category_by_name = graphene.Field(
    #     CategorizeType, name=graphene.String(required=True))

    def resolve_books(root, info):
        return Book.objects.select_related("category").all()

    def resolve_categorizes(root, info):
        return Categorize.objects.all()

    # def resolve_category_by_name(root, info, name):
    #     try:
    #         return Categorize.objects.get(name=name)
    #     except Categorize.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query)
