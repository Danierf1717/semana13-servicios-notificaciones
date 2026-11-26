from django.urls import path

from .views import lista_avisos


urlpatterns = [
    path("avisos/", lista_avisos, name="lista_avisos"),
]
