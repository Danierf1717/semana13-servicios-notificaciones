from django.contrib import admin

from .models import Aviso


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "creado_en")
    search_fields = ("titulo", "mensaje")
