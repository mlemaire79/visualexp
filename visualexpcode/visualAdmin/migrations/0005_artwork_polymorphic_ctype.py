# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 16:01

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def forwards_func(apps, schema_editor):
    Artwork = apps.get_model('visualAdmin', 'Artwork')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    new_ct = ContentType.objects.get_for_model(Artwork)
    Artwork.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)

def backwards_func(apps,schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('visualAdmin', '0004_auto_20160705_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_visualadmin.artwork_set+', to='contenttypes.ContentType'),
        ),

        migrations.RunPython(forwards_func, backwards_func)

    ]
