# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Lugares
from .serializer import LugaresSerializer

import json


class LugaresTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.firstLugar = Lugares.objects.create(nombre ='centro',calle = 'chapu',colonia = 'centro',codigo_postal = 1111)
        self.secondLugar = Lugares.objects.create(nombre ='centro2',calle = 'chapu2',colonia = 'centro2',codigo_postal = 1112)

        self.goodLugar ={
            'nombre':'centro2',
            'calle':'chapu2',
            'colonia':'centro2',
            'codigo_postal':2222
        }

        self.badLugar ={
            'nombre':'centro2',
            'calle':'chapu2',
            'colonia':'centro2',
            'codigo_postal':'2222'
        }

    def testGetAllLugares(self):
        response = self.client.get(reverse('lugares_endpoint'))
        personas = Lugares.objects.all()
        serialized = LugaresSerializer(personas,many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(serialized.data,response.data)
    
    ''' def testGetLugar(self):
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

    def testDeletePersona(self):
        response = self.client.delete(reverse('personas_endpoint',kwargs={'pk':self.secondPerson.id}))
        self.assertEqual(response.status_code,204)
    
    def testPutPersona(self):
        response = self.client.put(
            reverse('personas_endpoint',
            kwargs={'pk':self.firstPerson.id}),
            data=json.dumps(self.correct_person),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,202) '''
