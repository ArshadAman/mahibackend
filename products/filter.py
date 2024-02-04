# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['gte', 'lte'],
            'category__name': ['icontains'],
            'brand__name': ['icontains'],
            'color': ['icontains'],
            'size': ['icontains'],
            'is_featured': ['exact'],
        }
