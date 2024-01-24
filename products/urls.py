from django.urls import path
from . import views

urlpatterns = [
    path('add_category/', view=views.add_category, name='add_product'),
    path('delete_category/<uuid:pk>/', view=views.delete_category, name='delete-category'),
    path('all_category/', view=views.all_category, name='all_category'),
    
    # path('add_product/', view=views.add_product, name='add_product'),
    # path('delete_product/<uuid:pk>/', view=views.delete_product, name='delete-product'),
    # path('edit_product/<uuid:pk>/', view=views.edit_product, name='edit-product'),
    # path('view_product/<uuid:pk>/', view=views.view_product, name='view-product'),
]
