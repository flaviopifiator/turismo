# Generated by Django 2.1.4 on 2018-12-15 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0003_auto_20181215_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='capacitacion',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='capacitacion.Capacitacion'),
            preserve_default=False,
        ),
    ]