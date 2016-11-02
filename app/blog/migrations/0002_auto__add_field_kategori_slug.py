# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'kategori.slug'
        db.add_column(u'blog_kategori', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2014, 6, 6, 0, 0), max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'kategori.slug'
        db.delete_column(u'blog_kategori', 'slug')


    models = {
        u'blog.kategori': {
            'Meta': {'object_name': 'kategori'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kategori': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'blog.makale': {
            'Meta': {'object_name': 'makale'},
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'begenilme': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kategori': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.kategori']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'yazi': ('django.db.models.fields.TextField', [], {})
        },
        u'blog.yorum': {
            'Meta': {'object_name': 'yorum'},
            'begenilme': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icerik': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'makale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.makale']"}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'yapan': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['blog']