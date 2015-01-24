# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_auto_20150102_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('products', models.ManyToManyField(to='products.Product', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
