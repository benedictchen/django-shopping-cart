# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0006_auto_20150110_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='category',
            field=models.CharField(default=(b'size', b'size'), max_length=120,
                                   choices=[(b'size', b'size'), (b'color', b'color'), (b'package', b'package')]),
            preserve_default=True,
        ),
    ]
