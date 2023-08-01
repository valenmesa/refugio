from django.contrib import admin
from apps.mascota.models import Mascota, Vacuna
# from apps.mascota.apps import Vacuna

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Vacuna)

