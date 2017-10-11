# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lugares.models import Lugares

# Create your models here.

SEXOS =  (('M','Mujer'),('H','Hombre'),('I','Indefinido'))
TIPOS_PERSONAS= (('D','Damnificado'),('Voluntario','Voluntario'),('Otro','Otro'))
STATUS=(('1','Actual'),("0","Ya no"))

class Personas(models.Model) :
    nombre = models.CharField(max_length = 180)
    edad = models.IntegerField()
    sexo = models.CharField(choices= SEXOS, max_length = 5)
    tipo_de_personas = models.CharField(choices= TIPOS_PERSONAS, max_length=50)

class PersonasHasLugares(models.Model):
    fecha = models.DateField()
    status = models.CharField(max_length=2,choices=STATUS)
    persona_id = models.ForeignKey(Personas)
    lugar_id = models.ForeignKey(Lugares)