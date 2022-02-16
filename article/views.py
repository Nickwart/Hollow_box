from .models import Article
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ArticleSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    short_description = serializers.CharField(max_length=510)
    full_description = serializers.CharField(max_length=1024)
    price = serializers.IntegerField

    class Meta:
        model = Article
        fields = '__all__'


class ViewArticle(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'


class ViewAllArticles(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CreateArticle(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ArticleSerializer
