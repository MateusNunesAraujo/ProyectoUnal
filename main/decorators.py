from django.shortcuts import HttpResponse, redirect

#Decoradores en python:
#Los decoradores son funciones que modifican otras funciones. Cuando una función posee un decorador, el decorador es el que se ejecuta primero junto a la lógica adicional que integra.
#Como la función de un decorador es modificar funciones, entonces se debe pasar como parámetro principal la función que se va a modificar.

# Ejemplo básico de decorador:
""" def decorador(fun_principal):
    def logica_adicional(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return fun_principal(a, b)  # Llama a la función principal solo si ambos son pares
        return "Solo se permiten números pares"
    return logica_adicional #retorna la función anidada """

# Función principal
""" @decorador
def funcion_principal(a, b):
    resultado = a + b
    return resultado """

# Uso:
# funcion_principal(2, 4)  # Devuelve 6
# funcion_principal(2, 3)  # Devuelve "Solo se permiten números pares"

#Puntos clave:

#El decorador recibe la función principal como parámetro.Dentro del decorador, defines una función interna queimplementa la lógica adicional. La función interna debe llamar a la función principal si corresponde. El decorador retorna la función interna, no a sí mismo.


#En caso de las funciones decoradores en Django, lo único que cambia es que si o si, debe retornar un objeto tipo "HttpResponse", esto se consigue mediante funciones como "redirect()"
def solo_empresario(fun_view):
    def validacion(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "Empresario":
            return fun_view(request, *args, **kwargs)
        return redirect('login')
    return validacion

def solo_turistas(fun_view):
    def validacion(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role == "tourist":
            return fun_view(request,*args,**kwargs)
        return redirect('login')
    return validacion