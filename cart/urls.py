from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add_to_cart/<int:cereal_id>/<int:quantity>', views.add_to_cart, name="add-to-cart"),
    path('delete_from_cart/<int:cereal_id>', views.delete_from_cart, name='delete-from-cart'),
    path('update_quantity/<int:cereal_id>/<int:quantity>', views.update_quantity, name='update-quantity-cart'),
    path('clear', views.clear, name='clear-cart'),
    path('buy_single_item/<int:cereal_id>/<int:quantity>', views.buy_single_item, name='buy-single-item'),
    path('rebuy_order/<int:order_id>', views.rebuy_order, name='rebuy-order'),
    path('check_cart', views.check_cart, name='check-cart'),
    path('get_cart', views.get_cart, name='get-cart'),
]
