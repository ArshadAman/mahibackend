from rest_framework.serializers import ModelSerializer
from . import models
from django.contrib.auth.models import User

class AddressSerializer(ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = models.Wishlist
        fields = "__all__"

class CartItemSerializer(ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = "__all__"

class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = models.Cart
        fields = "__all__"

class CustomerSerializer(ModelSerializer):
    user = UserSerializer()
    addresses = AddressSerializer(many=True)
    wishlist = WishlistSerializer(many=True)
    cart = CartSerializer()

    class Meta:
        model = models.Customer
        fields = "__all__"
        
        
class UpdateProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Customer
        fields = ['user', 'phone_number']
        
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()

        return super().update(instance, validated_data)

        
        