from django.test import TestCase, RequestFactory
from article.views import CreateArticle, ViewArticle, ViewAllArticles
from article.models import Article


class OneArticleTestCase(TestCase):
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


class AllArticlesTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_all_articles_view(self):
        request = self.factory.get('shop/all')
        response = ViewAllArticles.as_view()(request)
        self.assertEqual(response.status_code, 200)


class CreateArticleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_of_article_creation(self):
        # test login first. need admin permissions to create articles
        article_data = {
            "product_name": "Sony DualSense",
            "short_description": "Nice phone, low price",
            "full_description": "2016 year of fub, Apple A12 processor, 13Mp camera",
            "price": 250,
        }
        request = self.factory.post('moderator/crestearticle')
        response = CreateArticle.as_view()(request, article_data)
        print(response.data)
        self.assertEqual(response.data, article_data)
    pass
