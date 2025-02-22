# Generated by Django 5.1.3 on 2024-12-12 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_archivo_registroactualizacion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='cargado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='archivo',
            name='usuario_carga',
            field=models.ForeignKey(blank=True, help_text='Usuario que cargo este archivo a la base de datos', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_usuario_carga', to=settings.AUTH_USER_MODEL),
        ),
    ]
