# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'kategori'
        db.create_table(u'blog_kategori', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kategori', self.gf('django.db.models.fields.CharField')(max_length=125)),
        ))
        db.send_create_signal(u'blog', ['kategori'])

        # Adding model 'makale'
        db.create_table(u'blog_makale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baslik', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('yazi', self.gf('django.db.models.fields.TextField')()),
            ('tarih', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('begenilme', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kategori', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.kategori'])),
        ))
        db.send_create_signal(u'blog', ['makale'])

        # Adding model 'yorum'
        db.create_table(u'blog_yorum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('makale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.makale'])),
            ('yapan', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('icerik', self.gf('django.db.models.fields.TextField')()),
            ('tarih', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('begenilme', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blog', ['yorum'])


    def backwards(self, orm):
        # Deleting model 'kategori'
        db.delete_table(u'blog_kategori')

        # Deleting model 'makale'
        db.delete_table(u'blog_makale')

        # Deleting model 'yorum'
        db.delete_table(u'blog_yorum')


    models = {
        u'blog.kategori': {
            'Meta': {'object_name': 'kategori'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kategori': ('django.db.models.fields.CharField', [], {'max_length': '125'})
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