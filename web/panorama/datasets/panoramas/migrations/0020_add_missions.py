# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panoramas', '0019_extra_indices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=24, unique=True)),
                ('type', models.CharField(choices=[('L', 'land'), ('W', 'water')], max_length=1)),
                ('date', models.DateField()),
                ('neighbourhood', models.TextField(max_length=50)),
            ],
        ),
    ]

