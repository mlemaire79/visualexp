# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualAdmin', '0013_auto_20160708_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundartwork',
            name='length',
            field=models.IntegerField(blank=True, null=True, verbose_name='Durée (en secondes)'),
        ),
        migrations.AlterField(
            model_name='videoartwork',
            name='length',
            field=models.IntegerField(blank=True, null=True, verbose_name='Durée (En secondes)'),
        ),
    ]
