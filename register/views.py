from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate
from login.models import *
from django.shortcuts import render

#Renderiza template para el registro de los usuarios
def register_view(request):
       return render(request, 'register.html')

#Crear usuarios
def create_user(request):
       if(request.POST["password_user"] == request.POST["confirm_password_user"]):
            user = User.objects.create(
                   username = request.POST['username_user'],
                   first_name = request.POST['primer_nombre'],
                   last_name = request.POST['apellidos'],
                   email = request.POST['email_user'],
                   role = 'tourist'  
                   )
            user.set_password(request.POST['password_user'])
            user.save()
            user_autenticado = authenticate(request, email=request.POST['email_user'], password=request.POST['password_user'])
            login(request,user_autenticado)
            return redirect('home')
       else:
              return render(request,"register.html",{"mensaje":"Las contraseñas no son iguales."})