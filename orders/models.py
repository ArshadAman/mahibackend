from django.db import models
import uuid
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    class Meta:
        ordering = ("-created_at",)
    
class OrderItem(models.Model):
    
    STATUS = (
        ('PLACED', 'PLACED'),
        ('PENDING', 'PENDING'),
        ('CANCELED', 'CANCELED'),
        ('FAILED', 'FAILED'),
        ('RETURN-REQUESTED', 'RETURN-REQUESTED'),
        ('RETURNED', 'RETURNED'),
    )
    
    PAYMENT_TYPE = (
        ('NA', 'NA'),
        ('PRE PAID', 'PRE PAID'),
        ('COD', 'COD'),
    )
    
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    customer = models.ForeignKey('customer.Customer', on_delete = models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete = models.CASCADE)
    status = models.CharField(max_length = 30, default = 'PENDING', choices = STATUS)
    payment_type = models.CharField(max_length = 10, choices = PAYMENT_TYPE, default = 'NA')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    

    class Meta:
        ordering = ("-created_at",)
    