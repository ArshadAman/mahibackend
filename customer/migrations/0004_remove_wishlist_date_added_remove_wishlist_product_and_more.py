# Generated by Django 5.0.1 on 2024-02-08 10:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_cart_total_amount'),
        ('products', '0009_alter_brand_id_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='customer.customer'),
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='customer.wishlist')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
