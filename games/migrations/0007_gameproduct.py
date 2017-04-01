# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20170329_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameProduct',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.Item')),
            ],
            bases=('games.item',),
        ),
    ]