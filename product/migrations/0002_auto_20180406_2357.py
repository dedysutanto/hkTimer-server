# Generated by Django 2.0.4 on 2018-04-06 16:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('display_item', models.PositiveIntegerField(default=0)),
                ('waste_item', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='click_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='display',
        ),
        migrations.RemoveField(
            model_name='product',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wasted',
        ),
        migrations.AddField(
            model_name='product',
            name='isClicked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(null=True),
        ),
        migrations.AddField(
            model_name='productcounter',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.Product'),
        ),
    ]
