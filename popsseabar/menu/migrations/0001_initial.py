# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('menu', models.ImageField(width_field='width', height_field='height', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('catering_price', models.DecimalField(decimal_places=2, verbose_name='Catering Price', max_digits=5)),
                ('market_price', models.BooleanField(default=False, verbose_name='Market Price')),
                ('is_active', models.BooleanField(default=True, verbose_name='Menu?')),
                ('catering_active', models.BooleanField(default=True, verbose_name='Catering?')),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]

