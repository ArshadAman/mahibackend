from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length = 255)
    price = models.IntegerField(default = 0)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)
    banner = models.ImageField(upload_to='category/banner/', null=True, blank=True)
    icon = models.ImageField(upload_to='category/icon/', null=True, blank=True)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length = 100, default = "Generic")
    logo = models.ImageField(upload_to="brand/logo", null=True, blank=True)
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)


class Product(models.Model):
    name = models.CharField(max_length = 255, null = True, blank = True)
    price = models.IntegerField(default = 0)
    mrp = models.IntegerField(default = 0)
    quantity = models.IntegerField(default=0)
    description = RichTextUploadingField(blank=True, null=True)
    image1 = models.ImageField(upload_to='product/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product/', null=True, blank=True)
    image5 = models.ImageField(upload_to='product/', null=True, blank=True)
    image6 = models.ImageField(upload_to='product/', null=True, blank=True)
    video_file = models.FileField(upload_to='product/videos/', null= True, blank=True)

    # Additional attributes for filtering
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, null = True)
    color = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    
    attributes = models.ManyToManyField(Attribute)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
    
    
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    
    def __str__(self):
        return self.name
    
    