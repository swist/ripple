# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'rippleapp_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('data', self.gf('picklefield.fields.PickledObjectField')(default=None)),
            ('musicbrainz_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('lastfm_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('soundcloud_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('fb_like_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('fb_page_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('social_media', self.gf('picklefield.fields.PickledObjectField')()),
            ('last_events', self.gf('picklefield.fields.PickledObjectField')()),
            ('aliases', self.gf('picklefield.fields.PickledObjectField')()),
            ('mbrainz_cache', self.gf('picklefield.fields.PickledObjectField')()),
        ))
        db.send_create_signal(u'rippleapp', ['Artist'])

        # Adding model 'Event'
        db.create_table(u'rippleapp_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('data', self.gf('picklefield.fields.PickledObjectField')(default=None)),
            ('lastfm_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'rippleapp', ['Event'])

        # Adding M2M table for field artists on 'Event'
        db.create_table(u'rippleapp_event_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'rippleapp.event'], null=False)),
            ('artist', models.ForeignKey(orm[u'rippleapp.artist'], null=False))
        ))
        db.create_unique(u'rippleapp_event_artists', ['event_id', 'artist_id'])

        # Adding model 'fbUser'
        db.create_table(u'rippleapp_fbuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('data', self.gf('picklefield.fields.PickledObjectField')(default=None)),
            ('f_uid', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('music_likes', self.gf('picklefield.fields.PickledObjectField')()),
            ('music_plays', self.gf('picklefield.fields.PickledObjectField')()),
            ('friends_ids', self.gf('picklefield.fields.PickledObjectField')()),
        ))
        db.send_create_signal(u'rippleapp', ['fbUser'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'rippleapp_artist')

        # Deleting model 'Event'
        db.delete_table(u'rippleapp_event')

        # Removing M2M table for field artists on 'Event'
        db.delete_table('rippleapp_event_artists')

        # Deleting model 'fbUser'
        db.delete_table(u'rippleapp_fbuser')


    models = {
        u'rippleapp.artist': {
            'Meta': {'object_name': 'Artist'},
            'aliases': ('picklefield.fields.PickledObjectField', [], {}),
            'data': ('picklefield.fields.PickledObjectField', [], {'default': 'None'}),
            'fb_like_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'fb_page_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_events': ('picklefield.fields.PickledObjectField', [], {}),
            'lastfm_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'mbrainz_cache': ('picklefield.fields.PickledObjectField', [], {}),
            'musicbrainz_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'social_media': ('picklefield.fields.PickledObjectField', [], {}),
            'soundcloud_id': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'rippleapp.event': {
            'Meta': {'object_name': 'Event'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events'", 'symmetrical': 'False', 'to': u"orm['rippleapp.Artist']"}),
            'data': ('picklefield.fields.PickledObjectField', [], {'default': 'None'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastfm_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
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