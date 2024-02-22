from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.\
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) # Username, email, Firstname, lastname, password
    phone_number = models.CharField(max_length = 12, blank = True, null = True)
    
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    
    def __str__(self) -> str:
        return f"{self.user.username}"
    

class Address(models.Model):
    
    ADDRESS_TYPE = (('Home', 'Home'), ('Work', 'Work'))
    
    customer = models.ForeignKey('Customer', related_name='addresses', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    alternate_phone_number = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    building_name = models.CharField(max_length=255, blank=True, null=True)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length = 20, choices = ADDRESS_TYPE, default = 'Home')
    
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return f"{self.name}, {self.city}, {self.state} {self.pincode}"
    
    
class WishlistItem(models.Model):
    wishlist = models.ForeignKey('Wishlist', on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    
    def __str__(self) -> str:
        return f'{self.wishlist.customer}\'s wishlist'
    
class Wishlist(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='wishlist')
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return f"wishlist of {self.customer}"
    
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    additional_price = models.PositiveIntegerField(default = 0)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return f"{self.product} ({self.quantity}) - {self.cart}"

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cart')
    
    total_amount = models.PositiveBigIntegerField(default=0)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return f"Cart for {self.customer}"

    