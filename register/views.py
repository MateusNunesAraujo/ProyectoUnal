from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.shortcuts import render

def register_view(request):
       return render(request, 'register.html')