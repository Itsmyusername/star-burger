# Generated by Django 3.2.15 on 2024-02-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeocodeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, unique=True, verbose_name='адрес')),
                ('lat', models.FloatField(null=True, verbose_name='широта')),
                ('lon', models.FloatField(null=True, verbose_name='долгота')),
                ('geocode_date', models.DateTimeField(auto_now=True, verbose_name='дата запроса к геокодеру')),
            ],
            options={
                'verbose_name': 'Данные геолокации',
                'verbose_name_plural': 'Данные геолокации',
                'unique_together': {('address',)},
            },
        ),
    ]
