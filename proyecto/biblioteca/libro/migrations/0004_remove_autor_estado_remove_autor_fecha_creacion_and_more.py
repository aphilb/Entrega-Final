# Generated by Django 4.0.5 on 2022-07-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_autor_estado_autor_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publicacion',
        ),
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]
