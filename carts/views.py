from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Cart
from products.models import Product


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart = Cart.objects.get(user=request.user)

    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart = Cart.objects.get(user=request.user)

    cart.items.remove(product)

    context = {'item': cart}
    return render(request, 'carts/delete.html', context)


@login_required
def remove_all_cart(request):
    cart = request.user.cart

    cart.items.clear()

    return redirect('cart')


@login_required
def cart(request):
    user = request.user

    products = user.cart.items.all()

    total_price = list(products.aggregate(Sum('price')).values())[0]

    context = {'products': products, 'total_price': total_price}
    return render(request, 'carts/cart.html', context)


@login_required
def deleteCart(request, pk):
    cart = Cart.objects.get(user=request.user)

    context = {'item': cart}
    return render(request, 'carts/delete.html', context)
