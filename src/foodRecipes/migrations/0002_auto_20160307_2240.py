# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-07 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodRecipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recept',
            name='datum_objave',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
