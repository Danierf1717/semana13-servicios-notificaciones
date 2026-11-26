from django.http import JsonResponse

from .models import Aviso


def lista_avisos(request):
    if request.method != "GET":
        return JsonResponse({"detail": "Método no permitido."}, status=405)

    datos = list(Aviso.objects.values("id", "titulo", "mensaje"))
    return JsonResponse(datos, safe=False)
