# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0007_auto_20141106_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='raw_html',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
