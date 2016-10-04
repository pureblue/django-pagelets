# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0011_auto_20141215_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('decription', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ('last_name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='author',
            field=models.ForeignKey(blank=True, null=True, to='pagelets.Author'),
            preserve_default=True,
        ),
    ]
