# Reporte técnico — Semana 13

**Alumno/a:** Daniel Ramirez Flores
**Grupo:** E-DAPM-2  
**Fecha:** [fecha de entrega]

## Proyecto y funcionamiento

Este ejemplo contiene una API Django que expone `GET /api/avisos/` como JSON y una app Android que recibe mensajes de Firebase Cloud Messaging (FCM) y construye una notificación con `NotificationCompat`. La app solicita el permiso de notificaciones en Android 13 o posterior cuando se pulsa el botón correspondiente.

**Repositorio GitHub:** https://github.com/Danierf1717/semana13-servicios-notificaciones
**APK o evidencia real de ejecución:** [adjunta el APK o capturas propias de la app y Logcat]

## Librerías y permisos

- Django: endpoint JSON y persistencia de avisos en SQLite.
- Firebase Messaging: recepción de mensajes push.
- AndroidX Core / `NotificationCompat`: creación de la notificación compatible.
- `POST_NOTIFICATIONS`: permiso de ejecución requerido desde Android 13.

## Evidencia verificada en este equipo

- El módulo interactivo fue abierto con la clave del grupo y el juego de Git quedó en el orden correcto.
- Las tres respuestas del quiz fueron resueltas con resultado correcto.
- La autoevaluación fue marcada y el módulo quedó registrado como completado el 26 de noviembre de 2026.
- La API Django respondió correctamente en `http://127.0.0.1:8000/api/avisos/` y devolvió JSON con un aviso de ejemplo:

```json
[{"id": 1, "titulo": "Clase cancelada", "mensaje": "Hoy no hay sesion de laboratorio"}]
```

- Las pruebas automatizadas de Django también se ejecutaron y resultaron en 2 pruebas aprobadas.

## Depuración y seguridad

La API tiene pruebas para respuesta JSON y rechazo de métodos distintos de GET. En Android se puede filtrar Logcat por `Semana13FCM`. No se incluyen credenciales Firebase en el repositorio: `google-services.json` está excluido mediante `.gitignore`. La clave de Django se configura mediante la variable de entorno `DJANGO_SECRET_KEY`.

**Pruebas que debes realizar antes de entregar:** ejecutar las pruebas Django; compilar e instalar la app en un emulador/dispositivo; permitir notificaciones; enviar un mensaje de prueba desde Firebase Console; guardar capturas propias de la notificación y Logcat. No reportes estos pasos como realizados hasta haberlos verificado.

## Uso de IA

- **Herramienta utilizada:** ChatGPT/Copilot (asistente de IA usado en esta conversación; indica el nombre que corresponda a la herramienta que viste).
- **Consulta realizada:** “vas a realizar esta actividad”, junto con las instrucciones completas de la actividad de Semana 13 pegadas en el chat. Después indiqué: “no lo tengo xd si quieres crealo, lo que creas necesario”.
- **Resultados obtenidos:** se completó el juego de orden de Git/GitHub y se respondieron las tres preguntas del quiz. También se generó un proyecto base con endpoint Django, pruebas automatizadas y código Android de ejemplo para FCM.
- **Análisis y justificación:** el orden y las respuestas del quiz se contrastaron con las explicaciones del módulo; la actividad confirmó cada selección como correcta. El código Django se debe validar ejecutando sus pruebas. El código Android todavía requiere configuración propia de Firebase y una prueba real en emulador o dispositivo; no se afirma que el APK o una notificación hayan sido ejecutados.
- **Aportación personal (completar con tus acciones reales):** [explica qué revisaste, cambiaste, probaste y qué evidencia generaste. No afirmes pruebas que no hayas realizado.]
