# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-11 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0018_remove_scalefile_is_operational'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
