# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class weapon(models.Model):
    utils_type_choices = (
            ('Sword' ,'sword'),
            ('Canon', 'canon'),
            ('Bazooka', 'bazooka'),
            )
    weapon_name = models.CharField(max_length = 20)
    weapon_image = models.ImageField(blank = True, upload_to = 'image')
    weapon_code = models.CharField(max_length = 20)
    utils_type = models.CharField(max_length = 20, choices = utils_type_choices)
    descriptions = models.TextField()
    created = models.DateTimeField(default = timezone.now)
    published = models.DateTimeField(blank = True, null = True)
    def published(self):
        self.published = timezone.now()
        self.save()
    def __unicode__(self):
        return self.weapon_name

class pilot(models.Model):
    gender_choices = (
            ('Male' ,'male'),
            ('Female', 'female'),
            ('Arturian', 'arturian'),
            )
    fractions_choices = (
            ('Alliance', 'alliance'),
            ('Federations', 'federations'),
            ('Mars', 'mars'),
            )
    name = models.CharField(max_length = 20)
    image = models.ImageField(blank = True, upload_to = 'image')
    code = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 20, choices = gender_choices)
    nationality = models.CharField(max_length = 20)
    bio = models.TextField()
    fractions = models.CharField(max_length = 20,choices = fractions_choices)
    created = models.DateTimeField(default = timezone.now)
    published = models.DateTimeField(blank = True, null = True)
    def published(self):
        self.published = timezone.now()
        self.save()
    def __unicode__(self):
        return self.name

class utils(models.Model):
    type_choices = (
            ('Aerial' ,'aerial'),
            ('Ground', 'ground'),
            ('Mariner', 'mariner'),
            )
    utils_name = models.CharField(max_length = 20)
    image = models.ImageField(blank = True, upload_to = 'image')
    utils_code = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20, choices = type_choices)
    descriptions = models.TextField()
    created = models.DateTimeField(default = timezone.now)
    published = models.DateTimeField(blank = True, null = True)
    def published(self):
        self.published = timezone.now()
        self.save()
    def __unicode__(self):
        return self.utils_name

class gundam(models.Model):
    type_choices = (
            ('Beast' ,'beast'),
            ('Attack', 'attack'),
            ('Surveillance', 'surveillance'),
            )
    name = models.CharField(max_length = 20)
    image = models.ImageField(blank = True, upload_to = 'image')
    descriptions = models.TextField(blank = True, null = True)
    code = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20, choices = type_choices)
    weapon = models.ForeignKey(weapon)
    pilot = models.ForeignKey(pilot)
    utils = models.ForeignKey(utils)
    created = models.DateTimeField(default = timezone.now)
    published = models.DateTimeField(blank = True, null = True)
    def published(self):
        self.published = timezone.now()
        self.save()
    def __unicode__(self):
        return self.name








