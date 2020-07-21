from django.urls import path
from .views import add_to_cart, cart, remove_cart, remove_all_cart, deleteCart


urlpatterns = [
    path('carts/', cart, name='cart'),
    path('carts/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('carts/remove_cart/<int:product_id>/',
         remove_cart, name='remove_cart'),
    path('carts/remove_all_cart/',
         remove_all_cart, name='remove_all_cart'),
    path('carts/deleteCart/<str:pk>/', deleteCart, name='deleteCart'),
]
