from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id,))

    def __str__(self):
        return self.title
