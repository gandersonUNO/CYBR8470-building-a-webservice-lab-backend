# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170924_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('size', models.CharField(max_length=1000)),
                ('friendliness', models.IntegerField()),
                ('trainability', models.IntegerField()),
                ('sheddingamount', models.IntegerField()),
                ('exerciseneeds', models.IntegerField()),
            ],
        ),
    ]
