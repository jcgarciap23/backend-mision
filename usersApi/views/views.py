from django.shortcuts import render
from django.http import HttpResponse

def prueba_usersApi(request):
    return HttpResponse('Hola desde users')