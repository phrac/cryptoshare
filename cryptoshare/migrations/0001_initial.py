# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'cryptoshare_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iv', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cryptoshare', ['Document'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'cryptoshare_document')


    models = {
        u'cryptoshare.document': {
            'Meta': {'object_name': 'Document'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iv': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['cryptoshare']