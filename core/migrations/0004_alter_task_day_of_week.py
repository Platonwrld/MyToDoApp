# Generated by Django 4.0.4 on 2022-06-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_task_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=15, null=True, verbose_name='День недели'),
        ),
    ]
