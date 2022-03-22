# Generated by Django 4.0.3 on 2022-03-22 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('subtitulo', models.CharField(max_length=20)),
                ('cuerpo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=20)),
                ('fechaCreacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('nombreUsuario', models.CharField(max_length=20)),
                ('contraseñaUsuario', models.CharField(max_length=30)),
            ],
        ),
    ]