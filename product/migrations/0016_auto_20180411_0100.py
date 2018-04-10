# Generated by Django 2.0.4 on 2018-04-10 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20180410_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCounterSummary',
            fields=[
            ],
            options={
                'verbose_name': 'ProductCounter Summary',
                'verbose_name_plural': 'ProductCounters Summary',
                'proxy': True,
                'indexes': [],
            },
            bases=('product.productcounter',),
        ),
        migrations.RemoveField(
            model_name='productcounter',
            name='uuid',
        ),
        migrations.AddField(
            model_name='productcounter',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
