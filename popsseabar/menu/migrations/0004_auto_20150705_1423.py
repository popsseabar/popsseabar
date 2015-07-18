# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20150702_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=sorl.thumbnail.fields.ImageField(verbose_name='Menu', upload_to='', width_field='width', height_field='height'),
        ),
    ]
