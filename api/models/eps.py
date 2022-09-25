from django.db import models
 
class Eps(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=30,unique=True)
    class Meta:
        ordering = ['nombre']