from  django.urls import re_path, include
from apps.adopcion.views import SolicitudList,SolicitudCreate,SolicitudUpdate,SolicitudDelete

urlpatterns = [
    re_path(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    re_path(r'^solicitud/nuevo$', SolicitudCreate.as_view(), name='solicitud_create'),
    re_path(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    re_path(r'^solicitud/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]