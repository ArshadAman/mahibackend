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

class CustomerSerializer(ModelSerializer):
    addresses = AddressSerializer(many = True)
    user = UserSerializer()
    class Meta:
        model = models.Customer
        fields = "__all__"
        
        
        
# Cart CartItem, Wishlist remaining 