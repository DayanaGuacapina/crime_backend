# Generated by Django 5.1.3 on 2024-12-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_archivo_cargado_archivo_usuario_carga'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='fecha_carga',
            field=models.DateField(blank=True, null=True),
        ),
    ]
