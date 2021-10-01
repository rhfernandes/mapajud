# Generated by Django 3.1.3 on 2021-05-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('cod_municipio_ibge', models.CharField(blank=True, max_length=50, null=True)),
                ('geo_m', models.CharField(max_length=1000)),
                ('cod_sigef', models.CharField(blank=True, max_length=50, null=True)),
                ('terrai_cod', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_floresta', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
    ]
