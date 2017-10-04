# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Personas, Lugares

from django.db import models

# Create your models here.

class Personas_Lugares(models.Model) :
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugares, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    status = models.CharField(max_lenght=2)
