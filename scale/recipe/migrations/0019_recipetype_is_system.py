# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0018_recipefile_recipe_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipetype',
            name='is_system',
            field=models.BooleanField(default=False),
        ),
    ]
