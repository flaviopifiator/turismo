# Generated by Django 2.1.4 on 2018-12-15 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0003_auto_20181215_1355'),
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='capacitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='capacitacion.Capacitacion'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor'),
        ),
    ]
