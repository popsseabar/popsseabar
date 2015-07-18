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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('our_story_copy', models.TextField()),
                ('address', models.TextField()),
                ('hours', models.TextField()),
                ('delivery_url', models.CharField(max_length=200)),
                ('gift_certificates_url', models.CharField(max_length=200)),
                ('email_signup_url', models.CharField(max_length=200)),
                ('alert_copy', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Options',
            },
        ),
    ]
