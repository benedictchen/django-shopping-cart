# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
