from django.urls import path
from . import views

urlpatterns = [
    path('siginup/', view=views.signup, name='signup'),
    path('get_profile/', view=views.get_profile, name='get_profile'),
    path('update_profile/', view=views.update_profile, name='update_profile'),
    path('add_address/', view=views.add_address, name='add_address'),
    path('update_address/', view=views.update_address, name='update_address'),
    path('view_all_addresses/', view=views.view_all_addresses, name='view_all_addresses'),
    path('add_to_cart/', view=views.add_to_cart, name='add_to_cart'),
    path('increase_cart_count/', view=views.increase_cart_count, name='increase_cart_count'),
    path('add_to_wishlist/', view=views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/', view=views.remove_from_wishlist, name='remove_from_wishlist'),
    path('buy_from_cart/', view=views.buy_from_cart, name='buy_from_cart'),
    path('buy_individual/', view=views.buy_individual, name='buy_individual'),
    path('cancel_order/', view=views.cancel_order, name='cancel_order'),
    path('return_order/', view=views.return_order, name='return_order'),
]
