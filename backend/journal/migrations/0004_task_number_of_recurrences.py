# Generated by Django 4.0.1 on 2022-02-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_task_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='number_of_recurrences',
            field=models.IntegerField(null=True),
        ),
    ]
