# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0008_page_raw_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='raw_js',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
