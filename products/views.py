from django.shortcuts import render
from django.utils import timezone
from .models import Product


# Create your views here.


def show_time(request):
    now = timezone.now()
    return render(request, 'show_time.html', {'now': now})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})
