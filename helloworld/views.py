# helloworld/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Usuario, Rescatado
from django.core import serializers
from django.http import JsonResponse
import json
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required

#rest framework
from rest_framework import generics
from .serializers import UsuarioSerializer, RescatadoSerializer


# Create your views here.
class UsuarioList(generics.ListCreateAPIView):
    try:
        queryset = Usuario.objects.all()
        serializer_class = UsuarioSerializer

        def get_object(self):
            queryset = self.get_queryset
            obj = get_object_or_404(
                queryset,
                pk=self.kwargs['pk'],
            )
            return obj
    except TypeError as ex:
        print("Error: "+str(ex))

class RescatadoList(generics.ListCreateAPIView):
    queryset = Rescatado.objects.all()
    serializer_class = RescatadoSerializer

    def get_object(self):
        queryset = self.get_queryset
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def index(request):
    rescatados = serializers.serialize('json', Rescatado.objects.all())
    return render(request, 'index.html', {"rescatados":json.loads(rescatados)})

@login_required(login_url='/login/') 
def dogsMantainer(request):
    rescatados = serializers.serialize('json', Rescatado.objects.all())
    return render(request, 'list.html', {"rescatados":json.loads(rescatados)})

@login_required(login_url='/login/')
def register_dogs(request):
    return render(request, 'register_dogs.html')

@login_required(login_url='/login/')
def createDogs(request):
    #try:
        photo = request.FILES.get('photo',False)
        name = request.POST.get('name')
        raza = request.POST.get('raza')
        description = request.POST.get('description')
        state = 'Disponible'
        dog = Rescatado(foto=photo,nombre=name,raza=raza,descripcion=description,state=state)
        dog.save()
        return HttpResponse('<script>alert("El perro ha sido inscrito correctamente..."); window.location.href="/list/";</script>')
    #except Exception as ex:
        #return HttpResponse('<script>alert("Se ha ingresado un valor incorrecto... Intenta nuevamente."); window.location.href="/register/dogs";</script>')

@login_required(login_url='/login/')
def delete_dogs(request, pk, template_name='dogs_confirm_delete.html'):
    dog = get_object_or_404(Rescatado, pk=pk)    
    if request.method=='POST':
        dog.delete()
        return redirect('/list/')
    return render(request, template_name, {'object':dog})

def createUser(request):
    try:
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        name = request.POST.get('name')
        born = request.POST.get('born')
        number = request.POST.get('number')
        region = request.POST.get('region')
        comuna = request.POST.get('comuna')
        house = request.POST.get('house')
        password = request.POST.get('password')

        user = Usuario(email=email, rut=rut, nombre=name, fecha_nacimiento=born, numero_telefono=number, region=region, comuna=comuna, tipo_casa=house, password=password)
        user.save()
        userAuth = User.objects.create_user(rut, email=email, password=password)
        userAuth.save()
        return HttpResponse('<script>alert("Usuario registrado correctamente!"); window.location.href="/login/";</script>')

    except Exception as ex:
        return HttpResponse('<script>alert("Se ha ingresado un valor incorrecto... Intenta nuevamente."); window.location.href="/register/";</script>')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto."); window.location.href="/";</script>')

def login_iniciar(request):
    usuario = request.POST.get('rut','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')
