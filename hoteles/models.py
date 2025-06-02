from django.db import models
from login.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
#Señales para cuando se elimine las imagenes
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Hoteles(models.Model):
    dueno = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(default=0)
    precio_noche = models.FloatField(default=0)
    descripcion = models.TextField(max_length=600)
    estrellas = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    ubicacion = models.TextField()
    """  resenas = models.IntegerField(default=0) """
    habitaciones = models.IntegerField(default=0,null=False)
    habitaciones_libres = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    class Meta:
        permissions = [("can_register_hotels", "Registrar hoteles")]

class ImagenesH(models.Model):
    fk_hoteles = models.ForeignKey(Hoteles,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="hoteles",null=True)

class Comentarios(models.Model):
    fk_hotel = models.ForeignKey(Hoteles,on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario = models.CharField(max_length=600)
    estrellas = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])


@receiver(post_delete, sender=ImagenesH)
def eliminar_archivo_imagen(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(False)