# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(default=1000.0, max_digits=300, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='tax_amount',
            field=models.DecimalField(default=1000.0, max_digits=300, decimal_places=2),
            preserve_default=True,
        ),
    ]
