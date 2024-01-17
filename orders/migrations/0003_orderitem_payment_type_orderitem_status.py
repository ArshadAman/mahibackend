# Generated by Django 5.0.1 on 2024-01-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_id_alter_orderitem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='payment_type',
            field=models.CharField(choices=[('NA', 'NA'), ('PRE PAID', 'PRE PAID'), ('COD', 'COD')], default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('PLACED', 'PLACED'), ('PENDING', 'PENDING'), ('CANCELED', 'CANCELED'), ('FAILED', 'FAILED'), ('RETURN-REQUESTED', 'RETURN-REQUESTED'), ('RETURNED', 'RETURNED')], default='PENDING', max_length=30),
        ),
    ]
