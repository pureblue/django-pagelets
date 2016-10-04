# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0009_page_raw_js'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='featured_image',
            field=models.FileField(blank=True, null=True, upload_to='featured-image/%Y/%m/%d/'),
            preserve_default=True,
        ),
    ]
