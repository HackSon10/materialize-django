# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-27 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_auto_20161120_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='comments/')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.Persona')),
            ],
        ),
    ]
