from django.urls import path
from .views import product_list, add_to_cart, view_cart, signup, user_logout, add_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('add-product/', add_product, name='add_product'),
]