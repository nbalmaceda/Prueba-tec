# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include 
from app import views, api
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from app.api import PrestamoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'prestamo', PrestamoViewSet)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", include("app.urls")),
    #path('api/prestamos/', api.PrestamoList.as_view()),
    #path('api/prestamos/<int:pk>/', api.PrestamoDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
