# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('carts', '0005_remove_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='carts.CartItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 6, 4, 10, 43, 296615, tzinfo=utc),
                                       auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 6, 4, 10, 56, 232218, tzinfo=utc),
                                       auto_now=True),
            preserve_default=False,
        ),
    ]
