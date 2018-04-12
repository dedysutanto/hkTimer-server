# Generated by Django 2.0.4 on 2018-04-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20180411_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcounter',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productcounter',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
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