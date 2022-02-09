from django.db import models


class Article(models.Model):
    product_name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=510)
    full_description = models.CharField(max_length=1024)
    price = models.IntegerField()


class CartModel(models.Model):
    pass
