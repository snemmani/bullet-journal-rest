# Generated by Django 3.1.3 on 2020-11-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='page',
            new_name='collection',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='due_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='page',
            new_name='collection',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='due_date',
            new_name='date',
        ),
        migrations.DeleteModel(
            name='Index',
        ),
    ]
