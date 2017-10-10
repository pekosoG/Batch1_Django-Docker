# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from personas.models import Personas

STATUS=(('1','Actual'),("0","Ya no"))

# Create your models here.

class Lugares(models.Model) :
    nombre = models.CharField(max_length = 180)
    calle = models.CharField(max_length = 50)
    colonia = models.CharField(max_length = 50)
    codigo_postal = models.IntegerField()
    #Geolocation Needed?


class PersonasHasLugares(models.Model):
    fecha = models.DateField()
    status = models.CharField(max_length=2,choices=STATUS)
    persona_id = models.ForeignKey(Personas)
    lugar_id = models.ForeignKey(Lugares)