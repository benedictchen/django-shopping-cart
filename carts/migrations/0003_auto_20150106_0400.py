# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_auto_20150102_0330'),
        ('carts', '0002_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 6, 4, 0, 18, 245558, tzinfo=utc),
                                       auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='carts.CartItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 6, 4, 0, 24, 477456, tzinfo=utc),
                                       auto_now=True),
            preserve_default=False,
        ),
    ]
