from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.



def restore_pass(request):
    if request.method == "POST":
        asunto = 'Recueprar Contraseña'
        mensaje = 'link de recuperacion:'
        de = settings.EMAIL_HOST_USER
        para = [request.POST['email_restore']]
        send_mail(asunto, mensaje, de, para)
        return redirect('/')

    return render(request, "usuarios/restore_pass.html")


def welcome(request):
    if request.user.is_authenticated:
        registros = Registro,object()
        context = {'registros': registros}
        return render(request, "usuarios/welcome.html", context)
    return redirect('/login')

def register(request):
    # se crea  el formulario para registro 
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            usuarios = form.save()

            if usuarios is not None:
                do_login(request, usuarios)
                return redirect('/')

    return render(request, "usuarios/register.html", {'form': form})

def login(request):
    # se crea el formulario 
    #recueperamos los valores
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            usuarios = authenticate(username=username, password=password)

            if usuarios is not None:
                do_login(request, usuarios)
                return redirect('/')

    return render(request, "usuarios/login.html", {'form': form})

def logout(request):
    # cerramos la sesión y madnamos al login
    do_logout(request)
    return redirect('/')