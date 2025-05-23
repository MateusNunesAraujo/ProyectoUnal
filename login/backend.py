from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import User

#En este archivo estamos creando un nuevo metodo de autenticación mediante una clase que hereda de una
#clase existente llamada "BaseBackend"
#Para el nuevo metodo, se crea una función con el nombre "authenticate" (esto es obligatorio para redefinir una función ya existente de la clase padre), luego pasamos los datos que desaeamos validar (email y contraseña). Del resto, es la logica para validar el usuario a través de los parametros que usemos en la función.
class MyBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email) #Obtenemos el email del usuario (nos devuelve un objecto del modelo User)
            if user.check_password(password): #Usando el objecto, podremos verificar la contraseña
                return user #Retornamos un objeto tipo "User"
            else:
                return None #Caso contrario, no retornamos nada
        except User.DoesNotExist: # Excepción si no encontramos usuarios con determinado emial
            return None
    
    #En estos archivos, es fundamental devolver un objeto completo, pero también necesitamos asociar el "ID" en caso de que el usuario se autentifique exitosamente, por eso debemos también de crear esta función llamda "get_user". 
    # Esto es necesario porque Django debe recuperar el ID por cada solicitud de obtención de datos del usuario. 
    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None