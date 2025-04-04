from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

user_login = "Mateus"
passw_login = "12345"

def hello_world(request,user,passw):
    global user_login,passw_login
    if user == user_login and passw_login == passw:
      
        return render(request,"index.html",{
            "nombre":user_login
            })
    else:
        return HttpResponse("Error")
    
