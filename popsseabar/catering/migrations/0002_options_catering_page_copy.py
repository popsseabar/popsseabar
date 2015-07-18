# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='catering_page_copy',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
