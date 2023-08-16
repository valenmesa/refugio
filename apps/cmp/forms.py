from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        
        fields = [
            "descripcion",
            "direccion",
            "contacto",
            "telefono",
            "email",
        ]
        labels={
            "descripcion":'Descripción',
            "direccion":'Dirección',
            "contacto":'Contacto',
            "telefono":'Telefono',
            "email": 'Email',
            'estado':'Estado'
            }
        exclude =[
            'um',
            'fm',
            'uc',
            'fc',
        ]
        widgets={
            'descripcion': forms.TextInput,
            # 'estado' : forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['estado'] = forms.BooleanField()