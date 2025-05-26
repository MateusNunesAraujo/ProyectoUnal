from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .models import User
from hoteles.models import Hoteles,ImagenesH
from main.decorators import solo_turistas

# Create your views here.


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


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login') 
    return render(request, 'index.html') 

@solo_turistas
def home(request):
    if request.user.is_authenticated:
        hoteles = Hoteles.objects.all()
        informacion = []
        for h in hoteles:
            imgs = ImagenesH.objects.filter(fk_hoteles=h)
            hotel = {
                "id":h.id,
                "nombre": h.nombre,
                "descripcion": h.descripcion,
                "ubicacion": h.ubicacion,
                "precio_noche": h.precio_noche,
                "estrellas_llenas": range(h.estrellas),
                "estrellas_vacias": range(5 - h.estrellas),
                "habitaciones": h.habitaciones,
                "resenas": h.resenas,
                "habitaciones_libres": h.habitaciones_libres,
                }
            informacion.append({"hotel": hotel, "imagenes": imgs})
        return render(request, "home.html", {"informacion": informacion})
    else:
        return redirect('login')

def info_hoteles(request,hotel_id):
    hotel = get_object_or_404(Hoteles,pk = hotel_id)
    imagenes = ImagenesH.objects.filter(fk_hoteles = hotel_id)
    print(imagenes)
    return render(request, "info_hotel.html",{"hotel":hotel,"imagenes": imagenes,"estrellas_llenas": range(hotel.estrellas), "estrellas_vacias": range(5 - hotel.estrellas)})

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

#Proximamente, agregarlo en una app de "eventos"
@solo_turistas
def eventos(request):
    return render(request, "eventos.html")

def info_eventos(request):
    return render(request, "info_eventos.html")
