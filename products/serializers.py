from rest_framework import serializers
from .models import Attribute, Category, Product

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"
