# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Lugares(models.Model) :
    nombre = models.CharField(max_length = 180)
    calle = models.CharField(max_length = 50)
    colonia = models.CharField(max_length = 50)
    codigo_postal = models.IntegerField(max_length = 6)
    #Geolocation Needed?
