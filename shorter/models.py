# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
import base64

# Create your models here.
class Url(models.Model):
    url = models.URLField(unique = True)
    #URLField mean TextField(validators=[URLValidator()])
    short_version = models.AutoField(primary_key=True)
    #primary_key inherits from previous concept.
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.url
        
    def get_short_url(self):
        data = base64.b64encode(str(self.short_version) )
        return reverse('redirecter', kwargs={'uri':data})

    def get_b64_number(self):
        data = base64.b64encode(str(self.short_version) )
        return data