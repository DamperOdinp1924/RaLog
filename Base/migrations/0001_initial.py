# Generated by Django 4.2.5 on 2023-09-27 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aerolineas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('Number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TarifasAerolineasFrutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaActualizacion', models.DateTimeField(null=True)),
                ('Conexion', models.TextField(max_length=10)),
                ('DSalida', models.TextField(max_length=10)),
                ('Min', models.DateField()),
                ('kg_100', models.IntegerField()),
                ('kg_300', models.IntegerField()),
                ('kg_500', models.IntegerField()),
                ('kg_1000', models.IntegerField()),
                ('kg_3000', models.IntegerField()),
                ('PMC', models.IntegerField()),
                ('PMCKG', models.IntegerField()),
                ('FS', models.IntegerField()),
                ('OTHERS', models.TextField(max_length=50)),
                ('Aerolineas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ATarifas', to='Base.aerolineas')),
                ('Carga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Carga', to='Base.carga')),
                ('Destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destino', to='Base.destino')),
                ('Origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Origen', to='Base.origen')),
                ('ResponsableActualizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroKg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('kg_100', models.IntegerField()),
                ('kg_300', models.IntegerField()),
                ('kg_500', models.IntegerField()),
                ('kg_1000', models.IntegerField()),
                ('kg_3000', models.IntegerField()),
                ('actualizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.tarifasaerolineasfrutas')),
            ],
        ),
    ]
