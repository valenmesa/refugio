from django.urls import include, path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, proveedor_inactivar




urlpatterns = [
    path(r'proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    path(r'proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path(r'proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path(r'proveedor/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),
]