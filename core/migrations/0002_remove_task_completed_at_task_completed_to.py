# Generated by Django 4.0.4 on 2022-05-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed_at',
        ),
        migrations.AddField(
            model_name='task',
            name='completed_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
