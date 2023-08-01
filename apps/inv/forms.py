from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        
        fields = [
            'descripcion',
            'estado'
        ]
        labels={
            'descripcion':'Descripción de la Categoría',
            'estado':'Estado'
        }
        widgets={
            'descripcion': forms.TextInput,
            'estado': forms.CheckboxSelectMultiple,   
        }
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            
