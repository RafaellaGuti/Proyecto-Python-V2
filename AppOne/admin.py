from django.contrib import admin
from AppOne.models import *
from .forms import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    form = Productosform

admin.site.register(Productos, ProductoAdmin)
admin.site.register(Servicios)
admin.site.register(Clientes)
admin.site.register(Avatar)



