# Generated by Django 4.2.2 on 2023-07-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic_Api', '0003_product_in_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='catagorys',
            field=models.ManyToManyField(to='Basic_Api.catagory'),
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ManyToManyField(to='Basic_Api.section'),
        ),
    ]
