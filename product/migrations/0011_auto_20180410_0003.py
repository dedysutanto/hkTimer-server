# Generated by Django 2.0.4 on 2018-04-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20180409_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcounter',
            name='end_time',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productcounter',
            name='start_time',
            field=models.BigIntegerField(default=0),
        ),
    ]
