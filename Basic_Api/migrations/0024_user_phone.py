# Generated by Django 4.2.2 on 2023-09-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Api', '0023_ourclient_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]