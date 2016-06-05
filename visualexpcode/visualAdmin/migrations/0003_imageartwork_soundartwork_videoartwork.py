# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualAdmin', '0002_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageArtwork',
            fields=[
                ('artwork_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('file', models.FileField(upload_to='image/')),
                ('artists', models.ManyToManyField(to='visualAdmin.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SoundArtwork',
            fields=[
                ('artwork_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('length', models.IntegerField(verbose_name='Length (in seconds) : ')),
                ('file', models.FileField(upload_to='video/')),
                ('artists', models.ManyToManyField(to='visualAdmin.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoArtwork',
            fields=[
                ('artwork_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('length', models.IntegerField(verbose_name='Length (in seconds) :')),
                ('file', models.FileField(upload_to='video/')),
                ('artists', models.ManyToManyField(to='visualAdmin.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
