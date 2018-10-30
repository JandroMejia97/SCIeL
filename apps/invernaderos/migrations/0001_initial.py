# Generated by Django 2.1.2 on 2018-10-24 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('Activado', models.BooleanField(verbose_name='Activado')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Actuadores',
                'verbose_name': 'Actuador',
            },
        ),
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('periodo_cosecha', models.IntegerField(verbose_name='Periódo de Cosecha')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Cultivo',
                'verbose_name': 'Cultivo',
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('nombre', models.CharField(max_length=45)),
                ('duracion', models.IntegerField(verbose_name='Duración de la etapa')),
                ('descripcion', models.CharField(max_length=150)),
                ('cultivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invernaderos.Cultivo')),
            ],
            options={
                'ordering': ['cultivo', 'numero', 'nombre'],
                'verbose_name_plural': 'Etapas',
                'verbose_name': 'Etapa',
            },
        ),
        migrations.CreateModel(
            name='Invernadero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('ubicacion', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magnitud', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Magnitud')),
                ('referencia', models.BooleanField(default=False, verbose_name='¿Es la referencia?')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de lectura')),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Parámetros',
                'verbose_name': 'Parámetro',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
    ]