# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Artist.lastfm_id'
        db.alter_column(u'rippleapp_artist', 'lastfm_id', self.gf('django.db.models.fields.CharField')(max_length=3072))

        # Changing field 'Artist.fb_like_id'
        db.alter_column(u'rippleapp_artist', 'fb_like_id', self.gf('django.db.models.fields.CharField')(max_length=3072))

        # Changing field 'Artist.soundcloud_id'
        db.alter_column(u'rippleapp_artist', 'soundcloud_id', self.gf('django.db.models.fields.CharField')(max_length=3072))

        # Changing field 'Artist.fb_page_id'
        db.alter_column(u'rippleapp_artist', 'fb_page_id', self.gf('django.db.models.fields.CharField')(max_length=3072))

        # Changing field 'Artist.musicbrainz_id'
        db.alter_column(u'rippleapp_artist', 'musicbrainz_id', self.gf('django.db.models.fields.CharField')(max_length=3072))

        # Changing field 'Event.lastfm_id'
        db.alter_column(u'rippleapp_event', 'lastfm_id', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Event.fb_id'
        db.alter_column(u'rippleapp_event', 'fb_id', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

    def backwards(self, orm):

        # Changing field 'Artist.lastfm_id'
        db.alter_column(u'rippleapp_artist', 'lastfm_id', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Artist.fb_like_id'
        db.alter_column(u'rippleapp_artist', 'fb_like_id', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Artist.soundcloud_id'
        db.alter_column(u'rippleapp_artist', 'soundcloud_id', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Artist.fb_page_id'
        db.alter_column(u'rippleapp_artist', 'fb_page_id', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Artist.musicbrainz_id'
        db.alter_column(u'rippleapp_artist', 'musicbrainz_id', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Event.lastfm_id'
        db.alter_column(u'rippleapp_event', 'lastfm_id', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Event.fb_id'
        db.alter_column(u'rippleapp_event', 'fb_id', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

    models = {
        u'rippleapp.artist': {
            'Meta': {'object_name': 'Artist'},
            'aliases': ('picklefield.fields.PickledObjectField', [], {}),
            'data': ('picklefield.fields.PickledObjectField', [], {'default': 'None'}),
            'fb_like_id': ('django.db.models.fields.CharField', [], {'max_length': '3072'}),
            'fb_page_id': ('django.db.models.fields.CharField', [], {'max_length': '3072'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_events': ('picklefield.fields.PickledObjectField', [], {}),
            'lastfm_id': ('django.db.models.fields.CharField', [], {'max_length': '3072'}),
            'mbrainz_cache': ('picklefield.fields.PickledObjectField', [], {}),
            'musicbrainz_id': ('django.db.models.fields.CharField', [], {'max_length': '3072'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'social_media': ('picklefield.fields.PickledObjectField', [], {}),
            'soundcloud_id': ('django.db.models.fields.CharField', [], {'max_length': '3072'})
        },
        u'rippleapp.event': {
            'Meta': {'object_name': 'Event'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'symmetrical': 'False', 'to': u"orm['rippleapp.Artist']"}),
            'data': ('picklefield.fields.PickledObjectField', [], {'default': 'None'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastfm_id': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'rippleapp.fbuser': {
            'Meta': {'object_name': 'fbUser'},
            'data': ('picklefield.fields.PickledObjectField', [], {'default': 'None'}),
            'f_uid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'friends_ids': ('picklefield.fields.PickledObjectField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_likes': ('picklefield.fields.PickledObjectField', [], {}),
            'music_plays': ('picklefield.fields.PickledObjectField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['rippleapp']