# Generated by Django 4.0.5 on 2022-07-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=220)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fechaDeNacimiento', models.DateField()),
            ],
        ),
    ]
