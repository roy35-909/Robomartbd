# Generated by Django 4.2.2 on 2023-08-04 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
