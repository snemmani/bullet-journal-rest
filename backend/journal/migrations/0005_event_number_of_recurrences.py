# Generated by Django 4.0.1 on 2022-02-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_task_number_of_recurrences'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='number_of_recurrences',
            field=models.IntegerField(null=True),
        ),
    ]
