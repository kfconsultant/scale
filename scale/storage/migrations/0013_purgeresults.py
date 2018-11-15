# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trigger', '0005_auto_20170412_1225'),
        ('storage', '0012_auto_20180920_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurgeResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_file_id', models.PositiveIntegerField(default=0)),
                ('num_jobs_deleted', models.PositiveIntegerField(default=0)),
                ('num_recipes_deleted', models.PositiveIntegerField(default=0)),
                ('num_products_deleted', models.PositiveIntegerField(default=0)),
                ('purge_started', models.DateTimeField(auto_now_add=True)),
                ('purge_completed', models.DateTimeField(blank=True, null=True)),
                ('trigger_event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trigger.TriggerEvent')),
            ],
            options={
                'db_table': 'purge_results',
            },
        ),
    ]