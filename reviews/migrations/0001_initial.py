# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 04:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0002_auto_20170412_1653'),
        ('member', '0007_merge_20170412_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_of_review', to='games.Game')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer_of_review', to='member.Member')),
            ],
        ),
    ]
