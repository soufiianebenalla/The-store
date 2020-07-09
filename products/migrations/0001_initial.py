# Generated by Django 3.0.7 on 2020-07-09 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 9, 3, 21, 41, 803075))),
            ],
        ),
    ]
