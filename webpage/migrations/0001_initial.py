# Generated by Django 4.0.5 on 2022-06-05 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('correo', models.TextField(max_length=50)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField()),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField(max_length=200)),
                ('alerta_bajo', models.BooleanField(default=False)),
                ('alerta_sobre', models.BooleanField(default=False)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_bajo', models.IntegerField()),
                ('nivel_sobre', models.IntegerField()),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.item')),
            ],
        ),
    ]
