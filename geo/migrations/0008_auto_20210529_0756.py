# Generated by Django 3.1.3 on 2021-05-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0007_processo_sirenejud'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
