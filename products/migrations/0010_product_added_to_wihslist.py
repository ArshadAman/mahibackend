# Generated by Django 5.0.1 on 2024-02-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_brand_id_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_to_wihslist',
            field=models.BooleanField(default=False),
        ),
    ]
