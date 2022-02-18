from django.db import models
from user_profile.models import ShopUser


class Article(models.Model):
    product_name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=510)
    full_description = models.CharField(max_length=1024)
    price = models.IntegerField()


class CartModel(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    item = models.ForeignKey(Article, on_delete=models.CASCADE)
    amount = models.IntegerField()
