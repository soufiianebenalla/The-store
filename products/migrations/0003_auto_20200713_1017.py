# Generated by Django 3.0.7 on 2020-07-13 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200709_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 13, 10, 17, 33, 981549)),
        ),
    ]
