# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_advert_prefered_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv',
            name='prod_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]