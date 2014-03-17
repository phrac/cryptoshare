# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Document.salt'
        db.alter_column(u'cryptoshare_document', 'salt', self.gf('django.db.models.fields.CharField')(max_length=64))

    def backwards(self, orm):

        # Changing field 'Document.salt'
        db.alter_column(u'cryptoshare_document', 'salt', self.gf('django.db.models.fields.CharField')(max_length=256))

    models = {
        u'cryptoshare.document': {
            'Meta': {'object_name': 'Document'},
            'ciphertext': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['cryptoshare']