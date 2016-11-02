# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'makale'
        db.create_table(u'blog_makale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baslik', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('yazi', self.gf('django.db.models.fields.TextField')()),
            ('tarih', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'blog', ['makale'])


    def backwards(self, orm):
        # Deleting model 'makale'
        db.delete_table(u'blog_makale')


    models = {
        u'blog.makale': {
            'Meta': {'object_name': 'makale'},
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'yazi': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['blog']