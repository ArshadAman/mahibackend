from rest_framework.serializers import ModelSerializer
from . import models
from django.contrib.auth.models import User
from customer.serializers import CustomerSerializer


class OrderSerializer(ModelSerializer):
    customer = CustomerSerializer
    class Meta:
        model = models.Order
        fields = "__all__"
        
class OrderItemSerializer(ModelSerializer):
    customer = CustomerSerializer()
    order = OrderSerializer()
    class Meta:
        model = models.OrderItem
        fields = "__all__"