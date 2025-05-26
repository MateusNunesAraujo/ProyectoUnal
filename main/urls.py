"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import *
from register.views import register_view
from hoteles.views import *
#Linea de codigo funcionales en etapa de DESARROLLO 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view,name='login'),
    path('register/',register_view, name="register"),  # URL para la vista de registro
    path('home/',home, name="home"),  # URL para la vista de inicio
    path("hoteles_registro/", home_hoteles_view, name="home_hoteles"),
    path('lista_hoteles/', lista_hoteles_view, name='lista_hoteles'),
    path('create_hotel/', create_hotel, name='create_hotel'),
    path("mostrar_hotel/",mostrar_hotel , name="mostrar_hotel"),
    path('update_hotel/<int:hotel_id>/', update_hotel, name='update_hotel'),
    path('delete_hotel/<int:hotel_id>/', delete_hotel, name='delete_hotel'),
    path('buscar_hotel/<str:nombre>/',buscar_hotel, name='buscar_hotel'),
    path("info_hoteles/<int:hotel_id>/", info_hoteles, name="info_hoteles"),
    path("filtrar/",filtrar, name="filtrar"),
    path("info_eventos/", info_eventos, name="info_eventos"),
    path('eventos/',eventos, name='eventos'),
    path('logout/',logout_view, name="logout")  # URL para la vista de login
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
