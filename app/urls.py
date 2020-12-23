# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from app import views
from django.contrib.auth.views import LoginView, logout_then_login #Vista de login Django
from django.contrib.auth.decorators import login_required
urlpatterns = [


    # The home page
    path('', views.index, name='index'),
    path('solicitud/prestamo/', views.solicitud_prestamo, name='solicitud_prestamo'),
    path('admin/list/prestamo/', login_required(views.list_prestamo), name='list_prestamo'),
    path('admin/editar/prestamo/<int:id_prestamo>/', login_required(views.editar_prestamo), name='editar_prestamo'),
    path('admin/borrar/prestamo/<int:id_prestamo>/', login_required(views.borrar_prestamo), name='borrar_prestamo'),
    path('admin/', LoginView.as_view(template_name='login.html'), name= 'login'),
    path('logout/', logout_then_login, name= 'logout'),


]
