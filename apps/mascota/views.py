from django.shortcuts import render
from django.http import HttpResponse
#Importamos el modelo
from apps.mascota.models import Mascota
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.mascota.form import MascotaForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    # return HttpResponse("Esta es la vista de mascotas")
    return render(request, "mascota/index.html")

# def mascota_list(request):
#     mascota= Mascota.objects.all()
#     contexto={'mascotas':mascota}
#     return render(request, "mascota/mascota_list.html", contexto)

class MascotaList(ListView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_list.html'
    paginate_by=2

# def mascota_view(request):
#     if request.method=='POST':
#         form=MascotaForm(request.POST)
#         if form.is_valid():
#             form.save()
#         # return redirect('mascota: index')
#         return redirect('mascota_listar')
#     else:
#         form=MascotaForm()
#     return render(request, "mascota/mascota_form.html", {'form':form})

#Crear registro
class MascotaCreate(CreateView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_form.html'
    success_url=reverse_lazy('mascota_listar')

# #Editar registro
# def mascota_edit(request, id_mascota):
#     mascota= Mascota.objects.get(id=id_mascota)
    
#     if request.method=='GET':
#         form=MascotaForm(instance=mascota)
        
#     else:
#         form=MascotaForm(request.POST, instance=mascota)
#         if form.is_valid():
#             form.save()
#         # return redirect('mascota: index')
#         mascota= Mascota.objects.all()
#         contexto={'mascotas':mascota}
#         return render(request, "mascota/mascot
# a_list.html", contexto)
#     return render(request, "mascota/mascota_form.html", {'form':form})

#Editar registro
class MascotaEdit(UpdateView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_form.html'
    success_url=reverse_lazy('mascota_listar')
    

# #Eliminar registro
# def mascota_delete(request, id_mascota):
#     mascota= Mascota.objects.get(id=id_mascota)
    
#     if request.method=='POST':
#         mascota.delete()
#         #return redirect('mascota: index')
#         return redirect('mascota_listar')
#     return render(request, "mascota/mascota_delete.html", {'mascota':mascota})

#Eilminar registro
class MascotaDelete(DeleteView):
    model=Mascota
    template_name='mascota/mascota_delete.html'
    success_url=reverse_lazy('mascota_listar')

