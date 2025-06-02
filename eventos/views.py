import json
from django.shortcuts import render,HttpResponse
from .models import *
from main.decorators import solo_turistas
from django.http import JsonResponse
from django.db.utils import IntegrityError

#Mostrar todos los eventos proximos.
@solo_turistas
def eventos(request):
    eventos = Eventos.objects.all()
    return render(request, "eventos.html",{"eventos":eventos})

#Mostrar información especifica de un evento.
@solo_turistas
def info_eventos(request,id):
    evento = Eventos.objects.get(pk = id)
    total_like = Like.objects.filter(evento=evento).count()
    return render(request, "info_eventos.html",{"evento":evento,"total_like":total_like})

#Sistema de dar like a un evento y quitar like (en caso de que el usuario ya tenga un like puesto en el evento)
@solo_turistas
def like(request):
    try:
        json_cargado = json.loads(request.body)
        evento = Eventos.objects.get(pk = json_cargado["id"])
        Like.objects.create(
            usuario = request.user,
            evento = evento
            )
        total_like = Like.objects.filter(evento = evento).count()
        return JsonResponse({"total_like":total_like})
    except IntegrityError:
        json_cargado = json.loads(request.body)
        evento = Eventos.objects.get(pk = json_cargado["id"])
        like = Like.objects.get(evento = evento, usuario = request.user)
        like.delete()
        total_like = Like.objects.filter(evento = evento).count()
        return JsonResponse({"error":"Error","total_like":total_like})

#Función temporal: Sirve para redirigir a plantillas estaticas donde muestrán galerias de fotos de eventos viejos (esta función se quitará una vez se cree un modelo para estos eventos viejos.)
def galeria_eventos(request,n):
    if n == 1:
        return render(request,"info_galeria_evento.html")
    elif n == 2:
        return render(request,"info_galeria_evento_leticia.html")  