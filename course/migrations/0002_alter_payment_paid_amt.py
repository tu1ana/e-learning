# Generated by Django 4.2.7 on 2023-11-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid_amt',
            field=models.PositiveIntegerField(verbose_name='Сумма оплаты'),
        ),
    ]
