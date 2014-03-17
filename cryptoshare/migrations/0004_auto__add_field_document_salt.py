# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Document.salt'
        db.add_column(u'cryptoshare_document', 'salt',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Document.salt'
        db.delete_column(u'cryptoshare_document', 'salt')


    models = {
        u'cryptoshare.document': {
            'Meta': {'object_name': 'Document'},
            'ciphertext': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cryptoshare']