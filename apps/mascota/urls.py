# from django.conf.urls import url, include
from django.urls import include, re_path
from apps.mascota.views import index, MascotaList , MascotaCreate, MascotaEdit, MascotaDelete
# , mascota_list, mascota_view, mascota_edit, mascota_list, MascotaEdit, mascota_delete

urlpatterns = [
    re_path(r'^$', index, name='index'),
    #re_path(r'^listar$', mascota_list, name='mascota_listar'),
    # re_path(r'^nuevo$', mascota_view, name='mascota_crear'),
    #re_path(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    #re_path(r'^eliminar/(?P<id_mascota>\d+)/$',mascota_delete, name='mascota_eliminar'),
    re_path(r'^nuevo$', MascotaCreate.as_view(), name='mascota_crear'),
    re_path(r'^listar$',  MascotaList.as_view(), name='mascota_listar'),
    re_path(r'^editar/(?P<pk>\d+)/$', MascotaEdit.as_view(), name='mascota_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),
]

