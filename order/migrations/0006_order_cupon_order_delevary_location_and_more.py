# Generated by Django 4.2.2 on 2023-09-01 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Api', '0022_cupon'),
        ('order', '0005_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Basic_Api.cupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='delevary_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.delivary'),
        ),
        migrations.AddField(
            model_name='order',
            name='price_after_add_copun',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
