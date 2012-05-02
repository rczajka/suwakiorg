# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slider'
        db.create_table('suwaki_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('suwaki', ['Slider'])

        # Adding model 'Value'
        db.create_table('suwaki_value', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['suwaki.Slider'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('suwaki', ['Value'])

        # Adding model 'News'
        db.create_table('suwaki_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['suwaki.Value'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('suwaki', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'Slider'
        db.delete_table('suwaki_slider')

        # Deleting model 'Value'
        db.delete_table('suwaki_value')

        # Deleting model 'News'
        db.delete_table('suwaki_news')


    models = {
        'suwaki.news': {
            'Meta': {'ordering': "['-date']", 'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suwaki.Value']"})
        },
        'suwaki.slider': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {})
        },
        'suwaki.value': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'Value'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suwaki.Slider']"})
        }
    }

    complete_apps = ['suwaki']
