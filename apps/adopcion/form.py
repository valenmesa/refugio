from django import forms
from apps.adopcion.models import Persona, Solicitud

class PersonaForm (forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels ={
            'nombre': 'Nombre',
            'apellido': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Teléfono',
            'email' :'Email',
            'domicilio':'Dirección',
        }
        Widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control'}),
        }

class SolicitudForm (forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels ={
            'numero_mascotas': 'Numero de mascotas',
            'razones': 'Razones para adoptar',
        }
        Widgets={
            'numero_mascotas': forms.TextInput(attrs={'class':'form-control'}),
            'razones': forms.Textarea(attrs={'class':'form-control'}),
        }