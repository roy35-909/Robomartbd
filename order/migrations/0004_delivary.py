# Generated by Django 4.2.2 on 2023-08-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
