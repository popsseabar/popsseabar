# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='section',
            field=models.ForeignKey(default='', to='menu.Section'),
            preserve_default=False,
        ),
    ]
