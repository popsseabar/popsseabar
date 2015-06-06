# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_item_market_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='item',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active?'),
        ),
        migrations.AlterField(
            model_name='item',
            name='market_price',
            field=models.BooleanField(default=False, verbose_name='Market Price'),
        ),
    ]
