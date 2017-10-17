# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Personas
from .serializer import PersonasSerializer

import json

class PersonasTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.firstPerson = Personas.objects.create(nombre='pepito',edad=22,sexo='H',tipo_de_personas='Otro')
        self.secondPerson = Personas.objects.create(nombre='pepita',edad=22,sexo='M',tipo_de_personas='Otro')

        self.correct_person={
            'nombre':'pepito',
            'edad':22,
            'sexo':'H',
            'tipo_de_personas':'Otro'
        }
        self.incorrect_person={
            'nombre':'pepito',
            'edad':2233,
            'sexo':'W',
            'tipo_de_personas':'Otro'
        }

    def testGetAllPersonas(self):
        response = self.client.get(reverse('personas_endpoint'))
        personas = Personas.objects.all()
        serialized = PersonasSerializer(personas,many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serialized.data,response.data)
    
    def testGetPersona(self):
        response = self.client.get(reverse('personas_endpoint', kwargs={'pk':self.firstPerson.id}))
        #response = self.client.get('/api/v1/personas/'+str(self.firstPerson.id)+'/')
        personas = Personas.objects.get(pk=self.firstPerson.id)
        serialized = PersonasSerializer(personas)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serialized.data,response.data)

    def testPostPersona(self):
        response = self.client.post(
            reverse('personas_endpoint'),
            data=json.dumps(self.correct_person),
            content_type='application/json')
        self.assertEqual(response.status_code,201)