# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 20:26
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panorama',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pano_id', models.CharField(max_length=37, unique=True)),
                ('timestamp', models.DateTimeField()),
                ('filename', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=400)),
                ('geolocation', django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326)),
                ('geolocation2D', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('roll', models.FloatField()),
                ('pitch', models.FloatField()),
                ('heading', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Traject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('geolocation', django.contrib.gis.db.models.fields.PointField(dim=3, srid=4326)),
                ('geolocation2D', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('north_rms', models.DecimalField(decimal_places=14, max_digits=20)),
                ('east_rms', models.DecimalField(blank=True, decimal_places=14, max_digits=20, null=True)),
                ('down_rms', models.DecimalField(blank=True, decimal_places=14, max_digits=20, null=True)),
                ('roll_rms', models.FloatField(blank=True, null=True)),
                ('pitch_rms', models.FloatField(blank=True, null=True)),
                ('heading_rms', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
