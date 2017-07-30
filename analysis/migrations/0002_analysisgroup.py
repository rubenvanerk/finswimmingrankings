# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 10:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rankings', '0003_auto_20170729_1144'),
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete', models.ManyToManyField(to='rankings.Athlete')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]