# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0006_auto_20141021_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubNav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('page', models.ManyToManyField(blank=True, to='pagelets.Page', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='inlinepagelet',
            name='order',
            field=models.SmallIntegerField(choices=[(-30, -30), (-29, -29), (-28, -28), (-27, -27), (-26, -26), (-25, -25), (-24, -24), (-23, -23), (-22, -22), (-21, -21), (-20, -20), (-19, -19), (-18, -18), (-17, -17), (-16, -16), (-15, -15), (-14, -14), (-13, -13), (-12, -12), (-11, -11), (-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], blank=True, null=True, help_text='The order in which pagelets should show up on the page. Lower numbers show up first.'),
        ),
        migrations.AlterField(
            model_name='pageattachment',
            name='order',
            field=models.SmallIntegerField(choices=[(-30, -30), (-29, -29), (-28, -28), (-27, -27), (-26, -26), (-25, -25), (-24, -24), (-23, -23), (-22, -22), (-21, -21), (-20, -20), (-19, -19), (-18, -18), (-17, -17), (-16, -16), (-15, -15), (-14, -14), (-13, -13), (-12, -12), (-11, -11), (-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sharedpagelet',
            name='order',
            field=models.SmallIntegerField(choices=[(-30, -30), (-29, -29), (-28, -28), (-27, -27), (-26, -26), (-25, -25), (-24, -24), (-23, -23), (-22, -22), (-21, -21), (-20, -20), (-19, -19), (-18, -18), (-17, -17), (-16, -16), (-15, -15), (-14, -14), (-13, -13), (-12, -12), (-11, -11), (-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], blank=True, null=True, help_text='The order in which pagelets should show up on the page. Lower numbers show up first.'),
        ),
    ]
