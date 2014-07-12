# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'fights_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('est_date', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'fights', ['Organization'])

        # Adding model 'Belt'
        db.create_table(u'fights_belt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('weight_class', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('boxing_organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='organization', to=orm['fights.Organization'])),
        ))
        db.send_create_signal(u'fights', ['Belt'])

        # Adding model 'Manager'
        db.create_table(u'fights_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'fights', ['Manager'])

        # Adding model 'Fighter'
        db.create_table(u'fights_fighter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('losses', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight_class', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('reach', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manager', to=orm['fights.Manager'])),
        ))
        db.send_create_signal(u'fights', ['Fighter'])

        # Adding model 'Bout'
        db.create_table(u'fights_bout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fighter1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fighter_one', null=True, to=orm['fights.Fighter'])),
            ('fighter2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fighter_two', null=True, to=orm['fights.Fighter'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bout_winner', blank=True, to=orm['fights.Fighter'])),
            ('fighter1_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fighter2_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'fights', ['Bout'])

        # Adding model 'Promoter'
        db.create_table(u'fights_promoter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('bout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='promoted_bout', blank=True, to=orm['fights.Bout'])),
        ))
        db.send_create_signal(u'fights', ['Promoter'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table(u'fights_organization')

        # Deleting model 'Belt'
        db.delete_table(u'fights_belt')

        # Deleting model 'Manager'
        db.delete_table(u'fights_manager')

        # Deleting model 'Fighter'
        db.delete_table(u'fights_fighter')

        # Deleting model 'Bout'
        db.delete_table(u'fights_bout')

        # Deleting model 'Promoter'
        db.delete_table(u'fights_promoter')


    models = {
        u'fights.belt': {
            'Meta': {'object_name': 'Belt'},
            'boxing_organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organization'", 'to': u"orm['fights.Organization']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'weight_class': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'fights.bout': {
            'Meta': {'object_name': 'Bout'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fighter1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fighter_one'", 'null': 'True', 'to': u"orm['fights.Fighter']"}),
            'fighter1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fighter2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fighter_two'", 'null': 'True', 'to': u"orm['fights.Fighter']"}),
            'fighter2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bout_winner'", 'blank': 'True', 'to': u"orm['fights.Fighter']"})
        },
        u'fights.fighter': {
            'Meta': {'object_name': 'Fighter'},
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manager'", 'to': u"orm['fights.Manager']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'reach': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight_class': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'fights.manager': {
            'Meta': {'ordering': "['name']", 'object_name': 'Manager'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'fights.organization': {
            'Meta': {'object_name': 'Organization'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'est_date': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'fights.promoter': {
            'Meta': {'ordering': "['name']", 'object_name': 'Promoter'},
            'bout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promoted_bout'", 'blank': 'True', 'to': u"orm['fights.Bout']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['fights']