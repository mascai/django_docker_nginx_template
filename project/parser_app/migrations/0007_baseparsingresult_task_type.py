# Generated by Django 4.0 on 2022-04-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0006_remove_basetask_is_active_basetask_is_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseparsingresult',
            name='task_type',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
