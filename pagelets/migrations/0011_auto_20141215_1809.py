# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0010_page_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subnav',
            name='page',
        ),
        migrations.DeleteModel(
            name='SubNav',
        ),
    ]
