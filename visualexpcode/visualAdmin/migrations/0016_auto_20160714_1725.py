# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-14 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualAdmin', '0015_auto_20160709_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(verbose_name='Biographie')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='visualAdmin.Artist')),
            ],
            options={
                'verbose_name': 'Artiste Translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'db_table': 'visualAdmin_artist_translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='artisttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
