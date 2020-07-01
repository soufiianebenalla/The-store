from django.db import models

# Create your models here.


class Product(models.model):
    title = models.CharField(max_length=100)
