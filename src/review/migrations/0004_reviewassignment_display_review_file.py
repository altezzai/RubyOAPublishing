# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-05 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20180208_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewassignment',
            name='display_review_file',
            field=models.BooleanField(default=False),
        ),
    ]
