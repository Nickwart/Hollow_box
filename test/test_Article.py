from django.test import TestCase, RequestFactory
from article.views import CreateArticle, ViewArticle
from article.models import Article


class ArticleTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.article1 = Article.objects.create(
            product_name="Iphone Xr",
            short_description="Nice phone, low price",
            full_description="2016 year of fub, Apple A12 processor, 13Mp camera",
            price=250,
        )
        self.article1.save()

    def test_article_exists(self):
        article1 = Article.objects.get(product_name='Iphone Xr')
        self.assertEqual(article1.short_description, "Nice phone, low price")
        self.assertEqual(article1.price, 250)

    def test_article_view(self):
        request = self.factory.get('/shop/<int:id>')
        response = ViewArticle.as_view()(request, id=self.article1.id)
        self.assertEqual(response.status_code, 200)
