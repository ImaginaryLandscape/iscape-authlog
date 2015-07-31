# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Access'
        db.create_table(u'authlog_access', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip_forward', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('get_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('post_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('http_accept', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('path_info', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('login_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'authlog', ['Access'])

        # Adding model 'AccessPage'
        db.create_table(u'authlog_accesspage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip_forward', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('get_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('post_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('http_accept', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('path_info', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('access_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('action_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'authlog', ['AccessPage'])


    def backwards(self, orm):
        # Deleting model 'Access'
        db.delete_table(u'authlog_access')

        # Deleting model 'AccessPage'
        db.delete_table(u'authlog_accesspage')


    models = {
        u'authlog.access': {
            'Meta': {'ordering': "['-login_time']", 'object_name': 'Access'},
            'get_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ip_forward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'login_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'authlog.accesspage': {
            'Meta': {'ordering': "['-access_time']", 'object_name': 'AccessPage'},
            'access_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'action_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'get_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ip_forward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['authlog']