from pyexpat import model
from django.db import models
from .eps import Eps
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    identification = models.CharField('Identification',max_length= 15,unique=True)
    apellidos = models.CharField('Apellidos',max_length=30,null=False)
    nombres = models.CharField('Nombres',max_length=30,null=False)
    direccion = models.CharField('Direcion',max_length=100,null=False)
    telefono = models.CharField('Telefono',max_length=20,null=False)
    correo = models.EmailField('Correo',max_length=100)
    edad = models.IntegerField(null=False)
    eps = models.ForeignKey(Eps,related_name='eps_estudiante',on_delete=models.PROTECT)
    adulto = models.BooleanField(null=False,default=True)
    genero = models.CharField('Gender',max_length=1)
    activo = models.BooleanField(default=True)
    comentario = models.TextField('Comentario',null=True)
    class Meta:
        ordering = ['apellidos']