from django.db import models

# Create your models here.
# from fights.models import *

class Organization(models.Model):
    name = models.CharField(max_length=120)
    acronym = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    est_date = models.CharField(max_length=4)

    def __unicode__(self):
        return u"{}".format(self.name)


class Belt(models.Model):
    name = models.CharField(max_length=120)
    weight_class = models.CharField(max_length=120)
    boxing_organization = models.ForeignKey(Organization, related_name='organization')


class Manager(models.Model):
    #one tourn has many groups
    #one group has many teams
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Managers"


class Fighter(models.Model):
    # one manager has many fighters
    # many fighters have one manager
    name = models.CharField(max_length=120)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    weight_class = models.CharField(max_length=120)
    reach = models.IntegerField(default=0)
    manager = models.ForeignKey(Manager, related_name='manager')

    def __unicode__(self):
        return u"{}".format(self.name)


class Bout(models.Model):
    # one game has two teams
    fighter1 = models.ForeignKey(Fighter, related_name='fighter_one', blank=True, null=True)
    fighter2 = models.ForeignKey(Fighter, related_name='fighter_two', blank=True, null=True)
    winner = models.ForeignKey(Fighter, related_name='bout_winner', blank=True, null=False)
    fighter1_score = models.IntegerField(default=0)
    fighter2_score = models.IntegerField(default=0)
    date = models.DateField(null=False)

    def __unicode__(self):
        return u"{} vs. {} - Winner: {}".format(self.fighter1, self.fighter2, self.winner)


class Promoter(models.Model):
    #one tourn has many groups
    #one group has many teams
    name = models.CharField(max_length=120)
    bout = models.ForeignKey(Bout, related_name='promoted_bout', blank=True, null=False)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Promoters"
