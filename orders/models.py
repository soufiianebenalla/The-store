from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product
from carts.models import Cart


User = get_user_model()


class Order(models.Model):
    user = models.OneToOneField(
        User, related_name='Order', on_delete=models.CASCADE)

    items = models.ManyToManyField(Cart, null=True, blank=True)

    order = models.ManyToManyField(Product, related_name='items')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
