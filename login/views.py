from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .models import User
from hoteles.models import Hoteles,ImagenesH,Comentarios
from main.decorators import solo_turistas

# Create your views here.

#Verifica el inicio de sesión de las personas que desean ingresar a la página
def login_view(request):
    if request.method == "POST":
        user_autenticado = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user_autenticado is not None:
            if user_autenticado.role == "tourist":
                print("Usuario autenticado")
                login(request, user_autenticado)
                return redirect("home")
            elif user_autenticado.role == "Empresario":
                print("Empresario autenticado")
                login(request, user_autenticado)
                return redirect("home_hoteles")
        else:
            print("Error")
            return render(request, "index.html",{"error":"Email o contraseña incorrectos"})
    return render(request, "index.html")    

#Cierre de sesión
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login') 
    return render(request, 'index.html') 

#Ingreso al home
@solo_turistas
def home(request):
    if request.user.is_authenticated:
        hoteles = Hoteles.objects.all()
        informacion = []
        for h in hoteles:
            imgs = ImagenesH.objects.filter(fk_hoteles=h)
            comentarios = Comentarios.objects.filter(fk_hotel = h).count()
            hotel = {
                "id":h.id,
                "nombre": h.nombre,
                "descripcion": h.descripcion,
                "ubicacion": h.ubicacion,
                "precio":h.precio,
                "precio_noche": h.precio_noche,
                "estrellas": h.estrellas,
                "estrellas_llenas": list(range(h.estrellas)),
                "estrellas_vacias": list(range(5 - h.estrellas)),
                "habitaciones": h.habitaciones,
                "resenas": comentarios,
                "habitaciones_libres": h.habitaciones_libres,
                }
            informacion.append({"hotel": hotel, "imagenes": imgs})
        return render(request, "home.html", {"informacion": informacion})
    else:
        return redirect('login')

#Mostrar información de hoteles especificos
def info_hoteles(request,hotel_id):
    info_comentarios = []
    hotel = get_object_or_404(Hoteles,pk = hotel_id)
    imagenes = ImagenesH.objects.filter(fk_hoteles = hotel_id)
    comentarios = Comentarios.objects.filter(fk_hotel = hotel)
    for c in comentarios:
        usuario = c.fk_usuario
        info_comentarios.append({"usuario":usuario,"id":c.pk,"comentario":c.comentario,"estrellas_llenas_c":list(range(c.estrellas)),"estrellas_vacias_c":list(range(5 - c.estrellas))})
    ya_comento = Comentarios.objects.filter(fk_hotel = hotel,fk_usuario = request.user).exists()
    print(imagenes)
    return render(request, "info_hotel.html",{"hotel":hotel,"imagenes": imagenes,"estrellas_llenas": range(hotel.estrellas), "estrellas_vacias": range(5 - hotel.estrellas),"comentarios":info_comentarios,"ya_comento":ya_comento})

#Buscar hotel
def buscar_hotel(request,nombre):
    """   list_imagenes = [] """
    try:
        hotel = Hoteles.objects.get(nombre__iexact=nombre)
    except Hoteles.DoesNotExist:
        hoteles = Hoteles.objects.all()
        informacion = []
        for h in hoteles:
            imgs = ImagenesH.objects.filter(fk_hoteles=h)
            informacion.append({"hotel": h, "imagenes": imgs})
        return render(request, "home.html", {"informacion": informacion})
    imagenes = ImagenesH.objects.filter(fk_hoteles = hotel)
    """   for img in imagenes:
        list_imagenes.append(img.imagen.url) """
    return render(request,"info_hotel.html",{"hotel":hotel,"imagenes":imagenes,"estrellas_llenas": range(hotel.estrellas),  "estrellas_vacias": range(5 - hotel.estrellas)})

#Renderizar template de los integrantes del proyecto
def nosotros_view(request):
    return render(request, "nosotros.html")

