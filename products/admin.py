from django.contrib import admin
from .models import Product

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at")


admin.site.register(Product)
