from django import forms
from apps.mascota.models import Mascota

class MascotaForm (forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'Persona',
            'vacuna',
        ]
        labels ={
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha del rescate',
            'Persona' :'adoptante',
            'vacuna':'Vacunas',
        }
        Widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.DateInput(attrs={'class':'form-control'}),
            'Persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
        }