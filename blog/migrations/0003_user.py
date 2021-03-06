# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-11 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=2)),
                ('address', models.TextField(null=True)),
                ('year', models.CharField(blank=True, max_length=50)),
                ('semester', models.CharField(blank=True, max_length=50)),
                ('std_id', models.CharField(blank=True, max_length=15)),
                ('session', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
