# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('carts', '0003_auto_20150106_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='active',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='updated_at',
        ),
    ]
