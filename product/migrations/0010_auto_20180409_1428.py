# Generated by Django 2.0.4 on 2018-04-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_left_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_time',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_time',
            field=models.BigIntegerField(default=0),
        ),
    ]
