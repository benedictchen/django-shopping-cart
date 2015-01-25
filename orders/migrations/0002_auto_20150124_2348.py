# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(default=0, max_digits=300, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='tax_amount',
            field=models.DecimalField(default=0, max_digits=300, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'started', max_length=255, choices=[(b'started', b'Started'), (b'abandoned', b'Abandoned'), (b'finished', b'Finished')]),
            preserve_default=True,
        ),
    ]
