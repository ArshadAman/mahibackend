from rest_framework import serializers
from .models import Attribute, Category, Product, Brand

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)
    category = CategorySerializer()
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = "__all__"
        
