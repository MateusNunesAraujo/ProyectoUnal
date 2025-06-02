import json
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import Hoteles, ImagenesH, Comentarios
from main.decorators import solo_empresario

# Create your views here.

#Renderiza el template de inicio
@solo_empresario
def home_hoteles_view(request):
    return render(request,"home_hoteles.html")

#Muestra todos los hoteles del usuario
@solo_empresario
def lista_hoteles_view(request):
    hoteles = Hoteles.objects.filter(dueno = request.user)
    return render(request,"lista_hoteles.html", {"hoteles": hoteles})

#Crea hoteles
@solo_empresario
def create_hotel(request):
    if request.method == "POST":
        hotel = Hoteles.objects.create(
            dueno=request.user,
            nombre=request.POST['nombre'],
            precio=request.POST['precio'],
            precio_noche=request.POST['precio_noche'],
            descripcion=request.POST['descripcion'],
            estrellas=request.POST['estrellas'],
            ubicacion=request.POST['ubicacion'],
            #resenas=request.POST['resenas'],
            habitaciones=request.POST['habitaciones'],
            habitaciones_libres=request.POST['habitaciones_libres'],
        )

        imagenes = request.FILES.getlist('imagenes')
        for img in imagenes:
            ImagenesH.objects.create(fk_hoteles=hotel, imagen=img)

        return redirect('lista_hoteles')
    return render(request,"create_hotel.html")

#Muestra información de un hotel en específico
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
        "precio":hotel.precio,
        "precio_noche": hotel.precio_noche,
        "estrellas":hotel.estrellas,
        "habitaciones":hotel.habitaciones,
        #r"resenas": hotel.resenas,
        "habitaciones_libres":hotel.habitaciones_libres,
        "img_urls":list_imagenes                   
                             })
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Actualiza la información de un hotel
@solo_empresario
def update_hotel(request,hotel_id):
    hotel = get_object_or_404(Hoteles, pk=hotel_id, dueno=request.user)
    if request.method == "POST":
        hotel.nombre = request.POST["nombre"]
        hotel.descripcion = request.POST["descripcion"]
        hotel.ubicacion = request.POST["ubicacion"]
        hotel.precio = request.POST["precio"]
        hotel.precio_noche = request.POST["precio_noche"]
        hotel.estrellas = request.POST["estrellas"]
        hotel.habitaciones = request.POST["habitaciones"]
        #rhotel.resenas = request.POST["resenas"]
        hotel.habitaciones_libres = request.POST["habitaciones_libres"]
        hotel.save()
        imagenes = request.FILES.getlist('imagenes')
        for img in imagenes:
            ImagenesH.objects.create(fk_hoteles = hotel, imagen = img)
        return redirect('lista_hoteles')
    return render(request,'update_hotel.html', {"hotel":hotel}) 

#Elimina un hotel
def delete_hotel(request,hotel_id):
    hotel = get_object_or_404(Hoteles, pk = hotel_id, dueno = request.user)    
    hotel.delete()
    hoteles = Hoteles.objects.filter(dueno = request.user)
    return render(request,'lista_hoteles.html', {"mensaje":"Eliminación exitosa","hoteles":hoteles})

#Filtra hoteles por estrellas o por rango de precios. 
def filtrar(request):
    json_cargado = json.loads(request.body)
    estrella = json_cargado["estrella"]
    precio_rango = json_cargado["precio_rango"]
    informacion = []

    hoteles = Hoteles.objects.all()

    if(json_cargado["estrella"] != "todos"):
        hoteles = hoteles.filter(estrellas = estrella)
        print("Resultados de ESTRELLAS")
    
    if(json_cargado["precio_rango"] != "todos"):
        if("mas" in precio_rango.split('-')):
             hoteles = hoteles.filter(precio_noche__gte=precio_rango.split('-')[0])
        else:
            min_precio, max_precio = map(int, precio_rango.split('-'))
            hoteles = hoteles.filter(precio__gte=min_precio, precio__lte=max_precio)
        print("Resultados de PRECIOS POR RANGOS")
    for h in hoteles:
        imagenes = ImagenesH.objects.filter(fk_hoteles = h)
        comentarios = Comentarios.objects.filter(fk_hotel = h).count()
        imagenes_urls = [img.imagen.url for img in imagenes]
        informacion.append({
        "id":h.id,
        "nombre": h.nombre,
        "descripcion": h.descripcion,
        "ubicacion": h.ubicacion,
        "precio": h.precio,
        "precio_noche": h.precio_noche,
        "estrellas": h.estrellas,
        "habitaciones": h.habitaciones,
         r"resenas": comentarios,
        "habitaciones_libres": h.habitaciones_libres,
        "img_urls": imagenes_urls
    })
    return JsonResponse({"informacion":informacion})

#Crea comentarios de unn usuario para un hotel
def create_comentarios(request):
    info_comentarios = []
    hotel = Hoteles.objects.get(pk = request.POST['id'])
    imagenes = ImagenesH.objects.filter(fk_hoteles = hotel)
    ya_comento = Comentarios.objects.filter(fk_hotel = hotel,fk_usuario = request.user).exists()
    if(not ya_comento):
        com = Comentarios.objects.create(
            fk_hotel =  hotel,
            fk_usuario = request.user,
            comentario = request.POST['comentario'],
            estrellas = request.POST['rating']
            ) 
    ya_comento = True
    comentarios = Comentarios.objects.filter(fk_hotel = hotel)
    print(ya_comento)
    for c in comentarios:
        usuario = c.fk_usuario
        info_comentarios.append({"usuario":usuario,"id":c.pk,"comentario":c.comentario,"estrellas_llenas_c":list(range(c.estrellas)),"estrellas_vacias_c":list(range(5 - c.estrellas))})
    
    return render(request, "info_hotel.html",{"hotel":hotel,"imagenes": imagenes,"estrellas_llenas": range(hotel.estrellas), "estrellas_vacias": range(5 - hotel.estrellas),"mensaje":"Comentario enviado exitosamente","comentarios":info_comentarios,"ya_comento":ya_comento})

#Elimina comentarios
def delete_comentarios(request,id,hotel_id):
    info_comentarios = []
    comentario = Comentarios.objects.get(pk = id).delete()
    hotel = Hoteles.objects.get(pk = hotel_id)
    imagenes = ImagenesH.objects.filter(fk_hoteles = hotel)
    ya_comento = Comentarios.objects.filter(fk_hotel = hotel,fk_usuario = request.user).exists()
    comentarios = Comentarios.objects.filter(fk_hotel = hotel)
    for c in comentarios:
        usuario = c.fk_usuario
        info_comentarios.append({"usuario":usuario,"comentario":c.comentario,"estrellas_llenas_c":list(range(c.estrellas)),"estrellas_vacias_c":list(range(5 - c.estrellas))})
    
    return render(request, "info_hotel.html",{"hotel":hotel,"imagenes": imagenes,"estrellas_llenas": range(hotel.estrellas), "estrellas_vacias": range(5 - hotel.estrellas),"mensaje":"Comentario eliminado exitosamente","comentarios":info_comentarios,"ya_comento":ya_comento})
