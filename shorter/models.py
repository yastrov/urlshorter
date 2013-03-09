# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=200)
    short_version = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.url
