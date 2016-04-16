# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-10 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodRecipes', '0002_auto_20160307_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='glavna_sestavina',
            field=models.CharField(choices=[('meso', 'Meso'), ('morska', 'Morski sadeži'), ('testenine', 'Testenine'), ('riž', 'Riž'), ('sadje', 'Sadje'), ('zelenjava', 'Zelenjava'), ('sir', 'Sir')], default='Meso', max_length=80),
        ),
    ]
