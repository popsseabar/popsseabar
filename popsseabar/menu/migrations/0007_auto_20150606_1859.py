# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20150601_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='position',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='section',
            name='position',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
