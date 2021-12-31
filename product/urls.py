from django.urls import path
from product.views import product,cart,update_cart


app_name = "product"

urlpatterns = [
    path('', product, name="product"),
    path('cart/', cart, name="cart"),
    path('update_cart/',update_cart,name="update_cart"),
]