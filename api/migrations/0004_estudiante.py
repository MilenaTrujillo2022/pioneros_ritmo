# Generated by Django 4.1 on 2022-09-25 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_eps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identification', models.CharField(max_length=15, unique=True, verbose_name='Identification')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direcion')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo')),
                ('edad', models.IntegerField()),
                ('adulto', models.BooleanField(default=True)),
                ('genero', models.CharField(max_length=1, verbose_name='Gender')),
                ('activo', models.BooleanField(default=True)),
                ('comentario', models.TextField(null=True, verbose_name='Comentario')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='eps_estudiante', to='api.eps')),
            ],
            options={
                'ordering': ['apellidos'],
            },
        ),
    ]
