from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proveedor,ComprasEnc, ComprasDet
from apps.inv.models import Producto
from .forms import ProveedorForm, ComprasEncForm
from django.urls import reverse_lazy
import json
from django.db.models import Sum
import datetime

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

def ProveedorInactivar(request, id):
    template_name="cmp/inactivar_prv.html"
    contexto={}
    prv=Proveedor.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse("Proveedor no existe" + str(id))
    
    if request.method=='GET':
        contexto={'obj': prv}
    
    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj': 'OK'}
        return HttpResponse("Proveedor Inactivado")
        
     
    return render(request, template_name, contexto)

class ComprasView(LoginRequiredMixin, generic.ListView):
    model=ComprasEnc
    template_name="cmp/compras_list.html"
    context_object_name="obj"
    login_url="login"

def compras(request, compra_id=None):
    template_name="cmp/compras.html"
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}
    
    if request.method=='GET':
        form_compras=ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()
        
        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra=datetime.date.isoformat(enc.fecha_compra)
            fecha_factura=datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra': fecha_compra,
                'proveedor':enc.proveedor,
                'observacion':enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            form_compras=ComprasEncForm(e)
        else:
            det=None
        contexto={'productos':prod, 'encabezado': enc, 'detalle':det, 'form_enc':form_compras}

    if request.method=='POST':

        fecha_compra=request.POST.get("fecha_compra")
        observacion=request.POST.get("observacion")
        no_factura=request.POST.get("no_factura")
        fecha_factura=request.POST.get("fecha_factura")
        proveedor=request.POST.get("proveedor")
        sub_total=0
        descuento=0
        total=0

        if not compra_id:
            prov=Proveedor.objects.get(pk=proveedor)

            enc= ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc=request.user
            )

            if enc:
                    enc.save()
                    compra_id=enc.id
        else:
            enc=ComprasEnc.ojects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra=fecha_compra
                enc.observacion=observacion
                enc.no_factura=no_factura
                enc.fecha_factura=fecha_factura
                enc.um=request.user.id
                enc.save()

        if not compra_id:
            return redirect("cmp: compras_list")

        producto=request.POST.get("id_id_producto")
        cantidad=request.POST.get("id_cantidad_detalle")
        precio=request.POST.get("id_precio_detalle")
        sub_total_detalle=request.POST.get("id_subtotal_detalle")
        descuento_detalle=request.POST.get("id_descuento_detalle")
        total_detalle=request.POST.get("id_total_detalle")

        prod=Producto.objects.get(pk=producto)

        det=ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
            uc=request.user
        )
        if det:
            det.save()

            subtotal=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total=sub_total["sub_total__sum"]
            enc.descuento=descuento["descuento__sum"]
        return redirect("cmp: compras_edit", compra_id=compra_id)

    return render(request, template_name, contexto)