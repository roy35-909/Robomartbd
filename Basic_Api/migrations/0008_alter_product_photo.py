# Generated by Django 4.2.2 on 2023-07-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Api', '0007_homepage_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
