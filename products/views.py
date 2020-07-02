from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product


# Create your views here.


def show_time(request):
    now = timezone.now()
    return render(request, 'show_time.html', {'now': now})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products-list.html',
                  {'products': products})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product-details.html',
                  {'product': product})
