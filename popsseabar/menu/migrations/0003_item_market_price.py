# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150524_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='market_price',
            field=models.BooleanField(default=False),
        ),
    ]
