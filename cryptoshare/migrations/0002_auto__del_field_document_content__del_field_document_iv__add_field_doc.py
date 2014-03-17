# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Document.content'
        db.delete_column(u'cryptoshare_document', 'content')

        # Deleting field 'Document.iv'
        db.delete_column(u'cryptoshare_document', 'iv')

        # Adding field 'Document.ciphertext'
        db.add_column(u'cryptoshare_document', 'ciphertext',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Document.content'
        db.add_column(u'cryptoshare_document', 'content',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)

        # Adding field 'Document.iv'
        db.add_column(u'cryptoshare_document', 'iv',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=256),
                      keep_default=False)

        # Deleting field 'Document.ciphertext'
        db.delete_column(u'cryptoshare_document', 'ciphertext')


    models = {
        u'cryptoshare.document': {
            'Meta': {'object_name': 'Document'},
            'ciphertext': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['cryptoshare']