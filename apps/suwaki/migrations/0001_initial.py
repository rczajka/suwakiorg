# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('suwaki_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dimension_length', self.gf('django.db.models.fields.IntegerField')()),
            ('dimension_control', self.gf('django.db.models.fields.IntegerField')()),
            ('dimension_enforcement', self.gf('django.db.models.fields.IntegerField')()),
            ('dimension_severity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('suwaki', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('suwaki_news')


    models = {
        'suwaki.news': {
            'Meta': {'ordering': "['-date']", 'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dimension_control': ('django.db.models.fields.IntegerField', [], {}),
            'dimension_enforcement': ('django.db.models.fields.IntegerField', [], {}),
            'dimension_length': ('django.db.models.fields.IntegerField', [], {}),
            'dimension_severity': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['suwaki']
