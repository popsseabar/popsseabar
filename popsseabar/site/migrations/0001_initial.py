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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('our_story_copy', models.TextField()),
                ('address', models.TextField()),
                ('hours', models.TextField()),
                ('delivery_url', models.CharField(max_length=200)),
                ('gift_certificates_url', models.CharField(max_length=200)),
                ('email_signup_url', models.CharField(max_length=200)),
                ('catering_orders_email', models.EmailField(max_length=254)),
                ('catering_email_confirmation_copy', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Options',
            },
        ),
    ]
