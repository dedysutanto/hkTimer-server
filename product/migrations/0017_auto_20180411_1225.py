# Generated by Django 2.0.4 on 2018-04-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20180411_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcounter',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productcounter',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
