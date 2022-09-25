from django.db import models
 
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=60,null=False, unique=True)
    duracion = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    class Meta:
        ordering = ['nombre']