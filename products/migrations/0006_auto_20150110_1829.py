# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0005_auto_20150106_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='image',
            field=models.ForeignKey(blank=True, to='products.ProductImage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100.0,
                                      validators=[django.core.validators.MinValueValidator(0)], max_digits=100,
                                      blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='variation',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 1, 10, 18, 29, 56, 318471, tzinfo=utc),
                                   max_length=120),
            preserve_default=False,
        ),
    ]
