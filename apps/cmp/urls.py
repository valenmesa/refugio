from django.urls import include, path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorInactivar,\
    ComprasView, compras



urlpatterns = [
    path(r'proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    path(r'proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path(r'proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    # path(r'proveedor/inactivar/<int:id>', proveedor_inactivar, name='proveedor_inactivar'),
    path(r'proveedor/inactivar/<int:id>', ProveedorInactivar, name='proveedor_inactivar'),
    
    path(r'compras/', ComprasView.as_view(), name='compras_list'),
    path(r'compras/new', compras, name='compras_new'),
    path(r'compras/edit/<int:compra_id>', compras, name='compras_edit'),
]