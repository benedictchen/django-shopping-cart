# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_cartitem_variations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'abc', unique=True, max_length=120)),
                ('status', models.CharField(max_length=255, choices=[(b'started', b'Started'), (b'abandoned', b'Abandoned'), (b'Finished', b'Finished')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(to='carts.Cart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
