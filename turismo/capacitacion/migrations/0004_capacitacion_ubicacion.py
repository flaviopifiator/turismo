# Generated by Django 2.1.4 on 2018-12-16 07:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0003_auto_20181215_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitacion',
            name='ubicacion',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
