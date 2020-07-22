from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)

    items = models.ManyToManyField(Product)

    address = models.CharField(max_length=500, default='')

    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        products = self.items.all()
        total_price = list(products.aggregate(Sum('price')).values())[0]

        return total_price

    def __str__(self):
        return f'{self.user.username}\'s order'
