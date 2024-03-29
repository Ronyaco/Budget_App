# Generated by Django 3.2.8 on 2023-03-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_auto_20220919_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Comments',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Job_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Last_Booking_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='New_Booking_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='Time_confirmed',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
