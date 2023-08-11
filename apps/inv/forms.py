from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

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

class SubCategoriaForm(forms.ModelForm):
    categoria=forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model=SubCategoria
        fields = [
            'categoria',
            'descripcion',
            'estado'
        ]
        labels={
            'descripcion':'Descripción de la SubCategoría',
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
        self.fields['categoria'].empty_label="Seleccione la Categoría"

class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        
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

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model=UnidadMedida
        
        fields = [
            'descripcion',
            'estado'
        ]
        labels={
            'descripcion':'Descripción de la unidad de medida',
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

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        
        fields = [
            'codigo',
            'codigo_barra',
            'descripcion',
            'estado',
            'precio',
            'existencia',
            'ultima_compra',
            'marca',
            'subcategoria',
            'unidadmedida'
        ]
        labels={
            'codigo':'Código',
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
           
            

        self.fields['ultima_compra'].widget.attrs['readonly']=True
        self.fields['existencia'].widget.attrs['readonly']=True
        self.fields['estado'] = forms.BooleanField()