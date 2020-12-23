# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Prestamo
from .forms import PrestamoForm
import sweetify
from django.db.models import Q
from django.core.paginator import Paginator
from .utils import *
   
def index(request):
    titulo = "Inicio"
    prestamos = Prestamo.objects.all()
    

    context = {
        "titulo":titulo,
        "inputs":prestamos,
    }

    return render (request, "index.html", context)

def list_prestamo(request):
    titulo = 'Prestamos'
    prestamos = Prestamo.objects.all()
    queryset = request.GET.get("dni_search")
    if queryset: 
        prestamos = Prestamo.objects.filter(
                Q(dni__icontains = queryset)
            )
    cant_prestamos = len(prestamos)
    paginator = Paginator(prestamos, 10) #Paginar de a 10 resultados
    page = request.GET.get('page')
    results = paginator.get_page(page)

    context = {
        "titulo":titulo,
        "prestamos":prestamos,
        "cant_prestamos":cant_prestamos,
        "results": results,
    }

    return render (request, "list_prestamo.html", context)

def solicitud_prestamo(request): # Guarda los datos del form solo si es aprobada la peticion
    titulo = 'Solicitud de Prestamo'
    form = PrestamoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form_data = form.cleaned_data #Obtengo los datos limpios del formulario
            nombre = form_data.get("nombre")
            apellido = form_data.get("apellido")
            dni = form_data.get("dni")
            sexo = form_data.get("sexo")
            email = form_data.get("email")
            monto = form_data.get("monto")
            persona_exist = Prestamo.objects.filter(dni=dni)
            status , has_error = get_prestamo(dni) # Comunicacion con API
            if persona_exist:
                sweetify.success(request, 'Info', icon='info',text='Usted ya tiene un prestamo asignado, para solicitar otro debe comunicarse con Atencion al Cliente 0800-MONI', persistent='Cerrar')
            elif status == "approve":
                messages.success(request, "Operacion Exitosa")
                sweetify.success(request, 'Felicitaciones', icon='success',text='Prestamo Aprobado para:'+"  "+nombre+" "+ apellido+" "+str(dni), persistent='Cerrar')
                form.save()
            elif( has_error == True ):
                messages.error(request, "Error de comunicacion intente mas tarde")
                sweetify.success(request, 'Error', icon='error',text='No hay comunicacion con el sistema', persistent='Cerrar')
            else:
                messages.error(request, "Operacion sin Exito")
                sweetify.success(request, 'Lo sentimos', icon='error',text='Prestamo desaprobado', persistent='Cerrar')    
        else:
                messages.error(request, str(form.errors))

        return redirect('index')


    context = {
        "titulo":titulo,
        "form": form,
    }

    return render(request, "solicitud_prestamo.html", context)

def editar_prestamo(request,id_prestamo):
    titulo = 'Editar Prestamo'
    prestamo = Prestamo.objects.get(id=id_prestamo)
    if request.method == 'GET':
        form= PrestamoForm(instance=prestamo)
    
    else:
        form= PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():

            form.save()
            sweetify.success(request, 'Editado', icon='success', persistent='Cerrar')
        else:
            messages.error(request, str(form.errors))
        return redirect('list_prestamo')

    context = {
        "titulo":titulo,
        "form": form,
    }
    return render (request, "solicitud_prestamo.html", context)    

def borrar_prestamo(request,id_prestamo):
    titulo = "Borrar Prestamo"
    prestamo = Prestamo.objects.get(id=id_prestamo)
    if request.method == 'POST':

        prestamo.delete()
        sweetify.success(request, 'Borrado', icon='success', persistent='Cerrar')   
        return redirect('list_prestamo')
    context = {
        "titulo":titulo,
        'prestamo':prestamo,
    }
    return render(request, "borrar_prestamo.html",context)