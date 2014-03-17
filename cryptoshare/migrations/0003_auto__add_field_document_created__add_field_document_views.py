# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Document.created'
        db.add_column(u'cryptoshare_document', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 17, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Document.views'
        db.add_column(u'cryptoshare_document', 'views',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Document.created'
        db.delete_column(u'cryptoshare_document', 'created')

        # Deleting field 'Document.views'
        db.delete_column(u'cryptoshare_document', 'views')


    models = {
        u'cryptoshare.document': {
            'Meta': {'object_name': 'Document'},
            'ciphertext': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cryptoshare']