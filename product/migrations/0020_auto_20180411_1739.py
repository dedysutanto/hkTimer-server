# Generated by Django 2.0.4 on 2018-04-11 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_productcounter_sold_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_file',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='isMainMenu',
            field=models.BooleanField(default=False),
        ),
    ]
