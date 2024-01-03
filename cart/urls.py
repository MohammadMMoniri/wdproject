from django.urls import path
from cart.views import add_to_cart, shopping_cart_view, remove_ticket

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('shopping-cart/', shopping_cart_view, name='shopping_cart'),
    path('remove_ticket/', remove_ticket, name='remove_ticket'),
    # path('finalize-cart/', finalize_cart, name='finalize_cart'),

]
