# Generated by Django 4.2.2 on 2023-08-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Api', '0017_remove_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
