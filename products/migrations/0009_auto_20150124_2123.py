# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150122_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(default=(b'size', b'Size'), max_length=120, choices=[(b'size', b'Size'), (b'color', b'Color'), (b'package', b'Package')]),
            preserve_default=True,
        ),
    ]
