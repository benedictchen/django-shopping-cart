# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150122_0807'),
        ('carts', '0007_auto_20150106_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(to='products.Variation', null=True, blank=True),
            preserve_default=True,
        ),
    ]
