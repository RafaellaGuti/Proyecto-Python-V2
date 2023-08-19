from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


def login_vista(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                mensaje = "Datos incorrectos"
                return render(request, "AppOS/login.html", {"form": form, "mensaje": mensaje})
    else:
        form = AuthenticationForm()

    return render(request, "AppOS/login.html", {"form": form})


