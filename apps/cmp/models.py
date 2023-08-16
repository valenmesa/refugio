from django.db import models
from apps.bases.models import ClassModelo

# Create your models here.
class Proveedor(ClassModelo):
    descripcion=models.CharField(max_length=100, unique=True)
    direccion=models.CharField(max_length=250, unique=True, blank=True)
    contacto=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10, unique=True, blank=True)
    email=models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion=self.descripcion.upper()
        super(Proveedor, self).save()
        
    class Meta:
        verbose_name_plural="Proveedores"