# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('catering_orders_email', models.EmailField(max_length=254)),
                ('catering_email_confirmation_copy', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Options',
            },
        ),
    ]
