# Generated by Django 3.2.4 on 2023-12-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0008_alter_factura_fecha_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_factura',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
