# Generated by Django 2.0.4 on 2018-04-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180407_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='displayed_item',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='wasted_time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
