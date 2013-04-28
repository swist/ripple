# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.tags'
        db.add_column(u'rippleapp_event', 'tags',
                      self.gf('picklefield.fields.PickledObjectField')(default=None),
                      keep_default=False)

        # Adding field 'Artist.tags'
        db.add_column(u'rippleapp_artist', 'tags',
                      self.gf('picklefield.fields.PickledObjectField')(default=None),
                      keep_default=False)

        # Adding field 'Artist.social_media'
        db.add_column(u'rippleapp_artist', 'social_media',
                      self.gf('picklefield.fields.PickledObjectField')(default=None),
                      keep_default=False)

        # Adding field 'Artist.aliases'
        db.add_column(u'rippleapp_artist', 'aliases',
                      self.gf('picklefield.fields.PickledObjectField')(default=None),
                      keep_default=False)

        # Adding field 'Artist.mbrainz_cache'
        db.add_column(u'rippleapp_artist', 'mbrainz_cache',
                      self.gf('picklefield.fields.PickledObjectField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.tags'
        db.delete_column(u'rippleapp_event', 'tags')

        # Deleting field 'Artist.tags'
        db.delete_column(u'rippleapp_artist', 'tags')

        # Deleting field 'Artist.social_media'
        db.delete_column(u'rippleapp_artist', 'social_media')

        # Deleting field 'Artist.aliases'
        db.delete_column(u'rippleapp_artist', 'aliases')

        # Deleting field 'Artist.mbrainz_cache'
        db.delete_column(u'rippleapp_artist', 'mbrainz_cache')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rippleapp.artist': {
            'Meta': {'object_name': 'Artist'},
            'aliases': ('picklefield.fields.PickledObjectField', [], {}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'artists'", 'symmetrical': 'False', 'to': u"orm['rippleapp.Event']"}),
            'fb_like_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'fb_page_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastfm_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'mbrainz_cache': ('picklefield.fields.PickledObjectField', [], {}),
            'musicbrainz_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'social_media': ('picklefield.fields.PickledObjectField', [], {}),
            'soundcloud_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {})
        },
        u'rippleapp.event': {
            'Meta': {'object_name': 'Event'},
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastfm_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {})
        },
        u'rippleapp.fbuser': {
            'Meta': {'object_name': 'fbUser', '_ormbases': [u'auth.User']},
            'f_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'f_location_id': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'f_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'friends': ('picklefield.fields.PickledObjectField', [], {}),
            'music_likes': ('picklefield.fields.PickledObjectField', [], {}),
            'music_plays': ('picklefield.fields.PickledObjectField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'fb_data'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['rippleapp']