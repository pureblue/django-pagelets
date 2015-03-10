# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0012_auto_20141216_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default='0'),
            preserve_default=True,
        ),
    ]
