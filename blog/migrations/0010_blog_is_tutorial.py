# Generated by Django 4.2.2 on 2023-10-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_blog_items_blogitems_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_tutorial',
            field=models.BooleanField(default=False),
        ),
    ]