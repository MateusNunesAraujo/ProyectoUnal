from django.db import models
from django.conf import settings

# Create your models here.

class Eventos(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion_corta = models.CharField(max_length=200,null=True)
    descripcion_larga = models.TextField()
    ubicacion = models.TextField()
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)
    hora_inicio = models.TimeField(default=0)
    hora_fin = models.TimeField(default=0)
    iframe_mapa = models.TextField(blank=True, null=True)
    imagen_principal = models.ImageField(upload_to="eventos",null=True)
    imagen_secundaria = models.ImageField(upload_to="eventos",null=True)

class Like(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'evento')

    def __str__(self):
        return f"{self.usuario.username} le dio like a {self.evento.nombre}"