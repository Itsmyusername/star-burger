# Generated by Django 3.2.15 on 2024-02-27 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0046_auto_20240226_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='selected_restaurant',
        ),
    ]
