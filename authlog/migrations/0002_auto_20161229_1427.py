# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesspage',
            name='action_type',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'OTHER'), (1, b'VIEW_CHANGE'), (2, b'SUBMIT_CHANGE'), (3, b'VIEW_DELETE'), (4, b'SUBMIT_DELETE'), (5, b'VIEW_HISTORY'), (6, b'VIEW_LIST'), (7, b'VIEW_ADD'), (8, b'SUBMIT_ADD'), (9, b'DOWNLOAD_CSV')]),
        ),
    ]
