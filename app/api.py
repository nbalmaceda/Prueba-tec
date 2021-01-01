# -*- encoding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
#from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from .models import Prestamo
from .serializers import PrestamoSerializer
#import io
#from rest_framework.views import APIView
from rest_framework import generics, viewsets
#from rest_framework.response import Response
#from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
'''
class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    
class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
'''
class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)