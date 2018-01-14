# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=45)),
                ('authors', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]