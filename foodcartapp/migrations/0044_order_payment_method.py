# Generated by Django 3.2.15 on 2024-02-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0043_auto_20240213_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('EL', 'Электронно'), ('CS', 'Наличностью')], default='CS', max_length=2),
        ),
    ]
