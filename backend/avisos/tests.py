import json

from django.test import TestCase

from .models import Aviso


class ListaAvisosTests(TestCase):
    def test_returns_avisos_as_json(self):
        aviso = Aviso.objects.create(
            titulo="Clase cancelada",
            mensaje="Hoy no hay sesión de laboratorio.",
        )

        response = self.client.get("/api/avisos/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(
            json.loads(response.content),
            [
                {
                    "id": aviso.id,
                    "titulo": "Clase cancelada",
                    "mensaje": "Hoy no hay sesión de laboratorio.",
                }
            ],
        )

    def test_rejects_non_get_requests(self):
        response = self.client.post("/api/avisos/")

        self.assertEqual(response.status_code, 405)
