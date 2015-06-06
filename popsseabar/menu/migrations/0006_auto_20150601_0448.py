# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20150527_0412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='section',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
    ]
