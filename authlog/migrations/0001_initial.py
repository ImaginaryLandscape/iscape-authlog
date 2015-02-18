# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30, null=True, blank=True)),
                ('user_agent', models.CharField(max_length=255, null=True, blank=True)),
                ('ip_address', models.CharField(max_length=255, null=True, verbose_name=b'IP Address', blank=True)),
                ('ip_forward', models.CharField(max_length=255, null=True, verbose_name=b'IP Forward Address', blank=True)),
                ('get_data', models.TextField(null=True, verbose_name=b'GET Data', blank=True)),
                ('post_data', models.TextField(null=True, verbose_name=b'POST Data', blank=True)),
                ('http_accept', models.CharField(max_length=255, null=True, verbose_name=b'HTTP Accept', blank=True)),
                ('path_info', models.CharField(max_length=255, null=True, verbose_name=b'Path', blank=True)),
                ('login_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-login_time'],
                'verbose_name': 'Login Access',
                'verbose_name_plural': 'Login Accesses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccessPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30, null=True, blank=True)),
                ('user_agent', models.CharField(max_length=255, null=True, blank=True)),
                ('ip_address', models.CharField(max_length=255, null=True, verbose_name=b'IP Address', blank=True)),
                ('ip_forward', models.CharField(max_length=255, null=True, verbose_name=b'IP Forward Address', blank=True)),
                ('get_data', models.TextField(null=True, verbose_name=b'GET Data', blank=True)),
                ('post_data', models.TextField(null=True, verbose_name=b'POST Data', blank=True)),
                ('http_accept', models.CharField(max_length=255, null=True, verbose_name=b'HTTP Accept', blank=True)),
                ('path_info', models.CharField(max_length=255, null=True, verbose_name=b'Path', blank=True)),
                ('access_time', models.DateTimeField(auto_now_add=True)),
                ('action_type', models.IntegerField(blank=True, null=True, choices=[(1, b'VIEW_CHANGE'), (2, b'SUBMIT_CHANGE'), (3, b'VIEW_DELETE'), (4, b'SUBMIT_DELETE'), (5, b'VIEW_HISTORY'), (6, b'VIEW_LIST'), (7, b'VIEW_ADD'), (8, b'SUBMIT_ADD'), (9, b'DOWNLOAD_CSV')])),
            ],
            options={
                'ordering': ['-access_time'],
                'verbose_name': 'Page Access',
                'verbose_name_plural': 'Page Accesses',
            },
            bases=(models.Model,),
        ),
    ]
