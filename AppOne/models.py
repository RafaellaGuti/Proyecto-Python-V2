from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='media/productos/', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Categoria: {self.categoria}  - Imagen: {self.imagen}"


class Servicios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Categoria: {self.categoria}"


class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    dni= models.IntegerField()
    email= models.EmailField()
    fechacompra= models.DateField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"



