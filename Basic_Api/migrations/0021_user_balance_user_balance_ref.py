# Generated by Django 4.2.2 on 2023-08-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Api', '0020_remove_user_is_admin_remove_user_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='balance_ref',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
