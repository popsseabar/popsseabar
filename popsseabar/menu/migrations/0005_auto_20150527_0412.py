# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20150524_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='catering_price',
            field=models.DecimalField(decimal_places=2, verbose_name='Catering Price', max_digits=5),
        ),
    ]
