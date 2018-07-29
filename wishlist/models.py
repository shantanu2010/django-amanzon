from django.db import models
from django.urls import reverse

from shop.models import Product
# Create your models here.


class Wishlist(models.Model):

    user_id = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    price = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

