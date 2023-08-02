from django.db import models
from apps.bases.models import ClassModelo

# Create your models here.
class Categoria(ClassModelo):
    descripcion=models.CharField(
        max_length=100,
        help_text='Descripción de Categoría', 
        unique=True
    )
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion=self.descripcion.upper()
        super(Categoria, self).save()
        
    class Meta:
        verbose_name_plural="Categorias"

class SubCategoria(ClassModelo):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion=models.CharField(
        max_length=100,
        help_text='Descripción de SubCategoría'
    )
    
    def __str__(self):
        return '{}'.format(self.categoria.descripcion, self.descripcion)
    
    def save(self):
        self.descripcion=self.descripcion.upper()
        super(Categoria, self).save()
        
    class Meta:
        verbose_name_plural="Sub Categorias"
        unique_together=('categoria', 'descripcion')