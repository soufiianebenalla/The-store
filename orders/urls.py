from django.urls import path

from .views import order_create, order_list


urlpatterns = [
    path('orders/', order_list, name='order_list'),
    path('orders/new/', order_create, name='order_create'),
]
