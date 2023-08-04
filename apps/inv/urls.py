from django.urls import include, path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel,\
    SubCategoriaView,SubCategoriaNew,SubCategoriaEdit,SubCategoriaDel,\
    MarcaView, MarcaNew, MarcaEdit, MarcaDel


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
    path(r'marca/delete/<int:pk>', MarcaDel.as_view(), name='marca_del'),
]
