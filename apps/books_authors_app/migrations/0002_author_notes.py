# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-17 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='this is a default text field value'),
            preserve_default=False,
        ),
    ]
