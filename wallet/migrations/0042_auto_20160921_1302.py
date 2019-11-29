# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 07:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0041_auto_20160918_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 10 digits allowed.', regex='^[789]\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='recharge',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 10 digits allowed.', regex='^[789]\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Numeric Field. Only 10 digits allowed.', regex='^[789]\\d{9}$')]),
        ),
    ]
