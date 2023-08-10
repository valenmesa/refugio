from django.urls import include, path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel,\
    SubCategoriaView,SubCategoriaNew,SubCategoriaEdit,SubCategoriaDel,\
    MarcaView, MarcaNew, MarcaEdit, marca_inactivar,\
    UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidadmedida_inactivar,\
    ProductoView, ProductoNew
    # ProductoEdit, producto_inactivar
    #MarcaDel


urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'categorias/', CategoriaView.as_view(), name='categoria_list'),
    path(r'categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path(r'categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path(r'categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),
    path(r'subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path(r'subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path(r'subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path(r'subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),
    path(r'marca/', MarcaView.as_view(), name='marca_list'),
    path(r'marca/new', MarcaNew.as_view(), name='marca_new'),
    path(r'marca/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path(r'marca/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),
    path(r'unidadmedida/', UnidadMedidaView.as_view(), name='unidadmedida_list'),
    path(r'unidadmedida/new', UnidadMedidaNew.as_view(), name='unidadmedida_new'),
    path(r'unidadmedida/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='unidadmedida_edit'),
    path(r'unidadmedida/inactivar/<int:id>', unidadmedida_inactivar, name='unidadmedida_inactivar'),
    path(r'producto/', ProductoView.as_view(), name='producto_list'),
    path(r'producto/new', ProductoNew.as_view(), name='producto_new'),
    # path(r'producto/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    # path(r'producto/inactivar/<int:id>', producto_inactivar, name='producto_inactivar'),
    # path(r'marca/delete/<int:pk>', MarcaDel.as_view(), name='marca_del'),
]
