from django.shortcuts import render, redirect, get_object_or_404
from AppOne.models import *
from AppOne.forms import *
from django.http import HttpResponse

#CRUD
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

#Login/Logout/Register
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #Para las clases
from django.contrib.auth.decorators import login_required #Para las funciones
from django.contrib.auth.views import LogoutView 
from django.utils.decorators import method_decorator

#Imagenes de Pillow
from PIL import Image
from django.conf import settings
import os

#Editar perfil
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

def inicio(request):
    return render(request, 'AppOne/inicio.html')

# Formularios

def productos(request):
    if request.method == "POST":
        miform = Productosform(request.POST, request.FILES)
        if miform.is_valid():
            informacion = miform.cleaned_data
            producto = Productos(nombre=informacion["nombre"], categoria=informacion["categoria"])
            producto.imagen = miform.cleaned_data['imagen']
            producto.save()
            return redirect('Inicio')
    else:
        miform = Productosform()

    return render(request, "AppOne/productos.html", {"miform": miform})


def clientes(request):
    if request.method == "POST":
        miform = Clientesform(request.POST)
        if miform.is_valid():
            informacion = miform.cleaned_data
            clientes = Clientes(nombre=informacion["nombre"], dni=informacion["dni"], email=informacion["email"], fechacompra=informacion["fechacompra"])
            clientes.save()
            return render(request, "AppOne/inicio.html")
    else:
        miform = Clientesform()

    return render(request, 'AppOne/clientes.html', {"miform": miform})


def servicios(request):
    if request.method == "POST":
        miform = Serviciosform(request.POST)
        if miform.is_valid():
            informacion = miform.cleaned_data
            servicios = Servicios(nombre=informacion["nombre"], categoria=informacion["categoria"])
            servicios.save()
            return redirect('Slist')
    else:
        miform = Serviciosform()

    return render(request, 'AppOne/servicios.html', {"miform": miform})

#Formulario Busqueda

def busquedacategoria(request):
      
    return render(request, 'AppOne/busquedacategoria.html')



def buscar(request):
    categoria = request.GET.get("categoria") 

    if categoria:
        productos = Productos.objects.filter(categoria__icontains=categoria)
        servicios = Servicios.objects.filter(categoria__icontains=categoria)

        return render(request, 'AppOne/resultadosbusqueda.html', {'productos': productos, 'categoria': categoria, 'servicios': servicios})
    else:
        respuesta = 'No enviaste datos'
        return render(request, 'AppOne/resultadosbusqueda.html', {'respuesta': respuesta})




#Vistas basadas en Clases
#Productos

class Productoslist(ListView):
    model = Productos
    template_name = 'AppOne/productos_list.html'
    context_object_name = 'productos'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Productos.objects.values_list('categoria', flat=True).distinct()
        return context

    

class Productosdetalle(DetailView):
    model= Productos
    template_name= 'AppOne/productos_detalle.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def resize_image(producto):
        if producto.imagen:
            image_path = os.path.join(settings.MEDIA_ROOT, producto.imagen.name)
            img = Image.open(image_path)
            img.thumbnail((300, 300))  # Redimensionar la imagen
            img.save(image_path)


class Productoscreacion(CreateView):
    model = Productos
    success_url = 'AppOne/productos/list'
    fields = ['nombre', 'categoria']

class Productosupdate(UpdateView):
    model = Productos
    fields = ['nombre', 'categoria']
    
    def get_success_url(self):
        return reverse_lazy('List')

class Productosdelete(DeleteView):
    model = Productos
    
    def get_success_url(self):
        return reverse_lazy('List')

#Categorias de productos
class CategoriaspList(ListView):
    model = Productos
    template_name = 'AppOne/categoriasp_list.html'
    context_object_name = 'categorias'


    def get_queryset(self):
        return Productos.objects.values_list('categoria', flat=True).distinct()


#Obtener productos por categoria
class ProductosPorCategoria(ListView):
    model = Productos
    template_name = 'AppOne/productos_por_categoria.html'
    context_object_name = 'productos'

    def get_queryset(self):
        # Obtén la categoría de la URL y filtra los productos por esa categoría
        categoria = self.kwargs['categoria']
        return Productos.objects.filter(categoria=categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega la variable 'categoria' al contexto para mostrarla en la plantilla
        context['categoria'] = self.kwargs['categoria']
        return context

#Servicios

class Servicioslist(ListView):
    model= Servicios
    template_name= 'AppOne/servicios_list.html'

    def get_queryset(self):
        return Servicios.objects.values_list('categoria', flat=True).distinct()

class Serviciosdetalle(DetailView):
    model= Servicios
    template_name= 'AppOne/servicios_detalle.html'

class Servicioscreacion(CreateView):
    model = Servicios
    success_url = 'AppOne/servicios/list'
    fields = ['nombre', 'categoria']

class Serviciosupdate(UpdateView):
    model = Servicios
    fields = ['nombre', 'categoria']
     
    def get_success_url(self):
        return reverse_lazy('Slist')

class Serviciosdelete(DeleteView):
    model = Servicios
    
    def get_success_url(self):
        return reverse_lazy('Slist')

#Categorias de servicios
class CategoriassList(ListView):
    model = Servicios
    template_name = 'AppOne/categoriass_list.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        # Obtén las categorías únicas y pásalas al contexto
        return Servicios.objects.values_list('categoria', flat=True).distinct()

#Obtener servicios por categoria
class ServiciosPorCategoria(ListView):
    model = Servicios
    template_name = 'AppOne/servicios_por_categoria.html'
    context_object_name = 'servicios'

    def get_queryset(self):

        categoria = self.kwargs['categoria']
        return Servicios.objects.filter(categoria=categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.kwargs['categoria']
        return context

#Registro

def register(request):

    if request.method == 'POST':

    
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return redirect('Login')

    else:
        form = UserRegisterForm()     

    return render(request,"AppOne/register.html" ,  {"form":form})


#Editar perfil

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()
            return render(request, "AppOne/inicio.html")
    else:
        form = UserEditForm(instance=usuario)

    return render(request, "AppOne/editarPerfil.html", {"form": form, "usuario": usuario})

#About
@login_required
def about(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppOne/about.html', {"url": avatares[0].imagen.url})

#Pagina en construccion
def paginacons(request):
    return render(request, 'AppOne/paginacons.html' )
