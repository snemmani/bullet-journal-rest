# Generated by Django 4.0.1 on 2022-02-02 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20201124_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task_page_rel', to='journal.journalcollection'),
            preserve_default=False,
        ),
    ]
