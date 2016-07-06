# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualAdmin', '0005_artwork_polymorphic_ctype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageartwork',
            name='artwork_ptr',
        ),
        migrations.RemoveField(
            model_name='soundartwork',
            name='artwork_ptr',
        ),
        migrations.RemoveField(
            model_name='videoartwork',
            name='artwork_ptr',
        ),
        migrations.DeleteModel(
            name='ImageArtwork',
        ),
        migrations.DeleteModel(
            name='SoundArtwork',
        ),
        migrations.DeleteModel(
            name='VideoArtwork',
        ),
    ]