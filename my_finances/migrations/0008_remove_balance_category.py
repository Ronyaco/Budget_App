# Generated by Django 3.2.8 on 2022-03-16 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0007_auto_20220313_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='category',
        ),
    ]