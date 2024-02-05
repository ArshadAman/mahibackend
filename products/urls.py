from django.urls import path
from . import views
from .views import ProductList

urlpatterns = [
    path('add_category/', view=views.add_category, name='add_product'),
    path('delete_category/<uuid:pk>/', view=views.delete_category, name='delete-category'),
    path('all_categories/', view=views.all_category, name='all_category'),
    path('all_brands/', view=views.all_brands, name='all_brands'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('product/<str:id>/', view=views.product_details, name="product-details")
    
    # path('add_product/', view=views.add_product, name='add_product'),
    # path('delete_product/<uuid:pk>/', view=views.delete_product, name='delete-product'),
    # path('edit_product/<uuid:pk>/', view=views.edit_product, name='edit-product'),
    # path('view_product/<uuid:pk>/', view=views.view_product, name='view-product'),
]

# /products/?name=keyword
# /products/?price__gte=50&price__lte=100
# /products/?category__name=category_name
# /products/?brand__name=brand_name
# /products/?color=color_name
# /products/?size=size_name
# /products/?is_featured=true
