# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150701_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='menu',
            new_name='url',
        ),
    ]
