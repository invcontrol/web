# Generated by Django 4.0.5 on 2022-06-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0006_alter_tipounidad_cssclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='algo',
            field=models.CharField(default='a', max_length=1),
            preserve_default=False,
        ),
    ]