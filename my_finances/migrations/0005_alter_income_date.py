# Generated by Django 3.2.8 on 2021-11-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0004_auto_20211029_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
