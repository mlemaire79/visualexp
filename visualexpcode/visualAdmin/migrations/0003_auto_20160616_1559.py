# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualAdmin', '0002_auto_20160616_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artists',
            new_name='artworks',
        ),
    ]
