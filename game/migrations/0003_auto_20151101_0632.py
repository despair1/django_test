# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_battle'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='combat_status',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='in_combat',
            field=models.ForeignKey(to='game.unit', null=True),
        ),
    ]
