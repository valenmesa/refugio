from django.contrib import admin
# from django.urls import path
from django.urls import re_path, include, path
from apps.mascota.views import index
from apps.adopcion.views import index
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^adopcion/', include('apps.adopcion.urls')),
    re_path(r'^mascota/', include('apps.mascota.urls')),
    re_path(r'^usuario/', include('apps.usuario.urls')),
    re_path(r'^accounts/login/', LoginView.as_view(template_name="usuario/index.html"), name="login"),
    re_path(r'^logout/', logout_then_login, name="logout"),
    path('inv/',include(('apps.inv.urls', 'inv'), namespace="inv")),
]
