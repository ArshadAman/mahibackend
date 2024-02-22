from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Coupon(models.Model):
    code =  models.CharField(max_length=6, blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.user.username} - {self.code}'

    def is_valid(self):
        return self.expiry_date > timezone.now()
