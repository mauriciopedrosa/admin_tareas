from enum import unique
from django.db import models
from django.contrib.auth.models import User

#### Usuario del sistema ADMIN ######

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion
    
    
class Area(models.Model):
    descripcion = models.CharField(max_length=100)
    nota = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descripcion
        
    
class Tarea(models.Model):
    usuario = models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200,null=False)
    descripcion = models.TextField(null=False)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria,null=False,on_delete=models.PROTECT)
    usuario_carga = models.CharField(max_length=61,null=True)
    area = models.ForeignKey(Area,null=False,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo

    # le defino una clase meta para establecer el orden de como quiero que se ordenen en la base
    class Meta:
        ordering = ['completo']
        
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    imagen = models.ImageField(upload_to= 'avatares', null= True, blank = True)

    def __str__(self):
        return f"Imagen de : {self.user}"