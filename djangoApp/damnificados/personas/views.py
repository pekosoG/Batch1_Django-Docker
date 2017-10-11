# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

from .models import Personas,PersonasHasLugares
from .serializer import PersonasGetName,PersonasCreateSerializer,PersonasSerializer,PersonasHasLugaresSerializer

import requests

# Create your views here.

class PersonasApi(APIView):

    def get(self, request):
        gente = Personas.objects.all()
        serializer = PersonasSerializer(gente, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        bato=PersonasSerializer(data=request.data)
        if bato.is_valid():
            bato.save()
            self._sendPush('asdasdasd','')
            return Response(bato.data,status=status.HTTP_201_CREATED)
        else:
            return Response(bato.errors, status=status.HTTP_400_BAD_REQUEST)

    def _sendPush(self,message, devicetoken):
        baseUrl = 'https://fcm.googleapis.com/fcm/send'
        header = {'Autorization':'key=AIzaSyB0k006LxEMxjpcL1bgz6CkAtEhX2UjQdY','Content-Type':'application/json'}
        body = { 'notification': { 'title': 'Dev-F!!!!!!!', 'body': 'SADOT! UNO NUEVO! ', 'icon': 'firebase-logo.png', 'click_action': 'https://haydetodo-test.firebaseapp.com/'}, 'to':'eV6hrH5oXgg:APA91bHb2GX6GYbj-VmtjtdvKlrsYur_emeJL9B6G0MJ8VSqUkY2F4p6CK58tg7S28XRc_NEaRoBGJ9uid1xGu43XHVs7-ySEBnbppaX0vJ0_ZU6W4jT_MtuVlxbtA3VVWGNBarM2yaj'}

        print('YEEEEEEEAAAAHHH')
        resp = requests.post(baseUrl,data=body,headers=header)  
        print('sdasdasd',resp)
    
class PersonaApi(APIView):
    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get(self, request, pk):
        persona = self._getPersona(pk)
        serialized = PersonasSerializer(persona)
        return Response(serialized.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        persona = self._getPersona(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonasHasLugaresApi(APIView):

    def get(self, request):
        lugar = PersonasHasLugares.objects.all()
        serializer = PersonasHasLugaresSerializer(lugar, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        lugar=PersonasHasLugaresSerializer(data=request.data)
        if lugar.is_valid():
            lugar.save()
            return Response(lugar.data,status=status.HTTP_201_CREATED)
        else:
            return Response(lugar, status=status.HTTP_400_BAD_REQUEST)