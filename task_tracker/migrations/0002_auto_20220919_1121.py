# Generated by Django 3.2.8 on 2022-09-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Hrs_Allocated',
        ),
        migrations.AlterField(
            model_name='task',
            name='Time_confirmed',
            field=models.CharField(max_length=50),
        ),
    ]