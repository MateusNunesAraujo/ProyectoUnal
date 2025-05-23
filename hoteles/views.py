import json
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Hoteles, ImagenesH
from main.decorators import solo_empresario

# Create your views here.

@solo_empresario
def home_hoteles_view(request):
    return render(request,"home_hoteles.html")

@solo_empresario
def lista_hoteles_view(request):
    hoteles = Hoteles.objects.filter(dueno = request.user)
    return render(request,"lista_hoteles.html", {"hoteles": hoteles})

@solo_empresario
def create_hotel(request):
    if request.method == "POST":
         # 1. Crear el hotel
        hotel = Hoteles.objects.create(
            dueno=request.user,
            nombre=request.POST['nombre'],
            precio_noche=request.POST['precio_noche'],
            descripcion=request.POST['descripcion'],
            estrellas=request.POST['estrellas'],
            ubicacion=request.POST['ubicacion'],
            resenas=request.POST['resenas'],
            habitaciones=request.POST['habitaciones'],
            habitaciones_libres=request.POST['habitaciones_libres'],
        )

        # 2. Guardar cada imagen asociada al hotel
        imagenes = request.FILES.getlist('imagenes')
        for img in imagenes:
            ImagenesH.objects.create(fk_hoteles=hotel, imagen=img)

        return redirect('lista_hoteles')  # Redirige a la lista de hoteles
    return render(request,"create_hotel.html")


def mostrar_hotel(request):
    list_imagenes = []
    data = json.loads(request.body)
    if request.method == "POST":
        hotel = Hoteles.objects.get(pk = data["id"])
        imagenes = ImagenesH.objects.filter(fk_hoteles=hotel)
        for img in imagenes:
            list_imagenes.append(img.imagen.url)
        return JsonResponse({
        "nombre": hotel.nombre,
        "descripcion":hotel.descripcion,
        "ubicacion": hotel.ubicacion,
        "precio_noche": hotel.precio_noche,
        "estrellas":hotel.estrellas,
        "habitaciones":hotel.habitaciones,
        "resenas": hotel.resenas,
        "habitaciones_libres":hotel.habitaciones_libres,
        "img_urls":list_imagenes                   
                             })
    return JsonResponse({"error": "Método no permitido"}, status=405)

@solo_empresario
def update_hotel(request,hotel_id):
    hotel = get_object_or_404(Hoteles, pk=hotel_id, dueno=request.user)
    if request.method == "POST":
        hotel.nombre = request.POST["nombre"]
        hotel.descripcion = request.POST["descripcion"]
        hotel.ubicacion = request.POST["ubicacion"]
        hotel.precio_noche = request.POST["precio_noche"]
        hotel.estrellas = request.POST["estrellas"]
        hotel.habitaciones = request.POST["habitaciones"]
        hotel.resenas = request.POST["resenas"]
        hotel.habitaciones_libres = request.POST["habitaciones_libres"]
        hotel.save()
        imagenes = request.FILES.getlist('imagenes')
        for img in imagenes:
            ImagenesH.objects.create(fk_hoteles = hotel, imagen = img)
        return redirect('lista_hoteles')
    return render(request,'update_hotel.html', {"hotel":hotel}) 

@solo_empresario
def delete_hotel(request,hotel_id):
    hotel = get_object_or_404(Hoteles, pk = hotel_id, dueno = request.user)
    hotel.delete()
    return render(request,'lista_hoteles.html', {"mensaje":"Eliminación exitosa"})

