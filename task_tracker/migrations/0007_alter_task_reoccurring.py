# Generated by Django 3.2.8 on 2023-03-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0006_auto_20230303_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reoccurring',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
