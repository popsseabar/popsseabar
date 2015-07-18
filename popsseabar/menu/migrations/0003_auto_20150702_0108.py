# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='', width_field='width', verbose_name='Menu', height_field='height'),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
