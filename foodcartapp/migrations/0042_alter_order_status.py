# Generated by Django 3.2.15 on 2024-02-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0041_auto_20240212_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PR', 'Обработать'), ('AS', 'Собрать'), ('TR', 'Доставить'), ('FN', 'Выполнен')], default='PR', max_length=2),
        ),
    ]
