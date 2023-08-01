from django.urls import include, path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel


urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'categorias/', CategoriaView.as_view(), name='categoria_list'),
    path(r'categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path(r'categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path(r'categorias/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),
]
