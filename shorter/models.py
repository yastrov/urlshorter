# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField()
    short_version = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.url
