# Generated by Django 2.1.2 on 2018-11-04 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invernaderos', '0002_cultivo_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='id_usuario',
            field=models.ForeignKey(blank=True, error_messages={'select': 'Debe seleccionar uno de la lista'}, help_text='Usuario al que pertenece este parametro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
