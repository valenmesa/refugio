from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proveedor
from .forms import ProveedorForm
from django.urls import reverse_lazy

import json

# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model=Proveedor
    template_name="cmp/proveedor_list.html"
    context_object_name="obj"
    login_url="login"
    
class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name="obj"
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')
    login_url="login"
    
    def form_valid(self, form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name="obj"
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')
    login_url="login"
    
    def form_valid(self, form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)


def proveedor_inactivar(request,id):
    template_name="cmp/proveedor_inactivar.html"
    contexto={}
    # se crea una variable llamada, en este caso se llamo prv
    prv=Proveedor.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Proveedor no existe" + str(id))
    if request.method=='GET':
        contexto={'obj': prv}
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        return HttpResponse("Proveedor Inactivado" )
    return render(request, template_name, contexto)

# def proveedor_inactivar(request,id):
#     producto=Producto.objects.filter(pk=id).first()
#     contexto={}
#     template_name="inv/estado_inactivar.html"
#     if not producto:
#         return redirect("inv:producto_list")

#     if request.method=='GET':
#         context={'obj':producto}

#     if request.method=='POST':
#         producto.estado=False
#         producto.save()
#         return redirect("inv:producto_list")

#     return render(request, template_name, contexto)