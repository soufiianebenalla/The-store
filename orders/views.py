from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Order
from .forms import OrderCreateForm
from .utils import send_order_email


@login_required
def order_create(request):
    user = request.user

    if not user.cart.items.exists():
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(user)
            send_order_email(request, user, order)
            return render(request, 'orders/order_success.html')

    else:
        form = OrderCreateForm()

    context = {'form': form}
    return render(request, 'orders/order_create.html', context)


def order_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        order_create = Order.objects.all()

        context = {'order_create': order_create}
        return render(request, 'orders/order_list.html', context)
    else:
        return redirect('product_list')
