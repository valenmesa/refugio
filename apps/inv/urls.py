from django.urls import include, path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView,SubCategoriaNew,SubCategoriaEdit,SubCategoriaDel


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
]
