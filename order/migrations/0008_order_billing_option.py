# Generated by Django 4.2.2 on 2023-09-17 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_is_payment_done_order_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_option',
            field=models.CharField(default='CASH_ON_DELIVERY', max_length=100),
        ),
    ]
