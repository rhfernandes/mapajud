# Generated by Django 3.1.3 on 2021-05-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0005_processo_cod_municipio_ibge'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='sicar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
