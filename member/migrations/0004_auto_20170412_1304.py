# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20170411_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='accumulating_spending',
            new_name='accumulated_spending',
        ),
    ]
