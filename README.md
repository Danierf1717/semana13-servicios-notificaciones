# Semana 13: servicios, notificaciones y API

Proyecto de práctica para la actividad de cierre de la Unidad III. Incluye una API Django para avisos y el código de una app Android que recibe mensajes FCM y muestra notificaciones.

## API Django

Requiere Python 3.10 o posterior.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:DJANGO_SECRET_KEY = "reemplaza-por-una-clave-local"
python manage.py migrate
python manage.py test
python manage.py runserver
```

Consulta `http://127.0.0.1:8000/api/avisos/`. La respuesta es una lista JSON; inicialmente estará vacía. Para agregar datos, crea un superusuario, entra a `/admin/` y registra avisos.

## App Android / FCM

1. Crea una app Android en Firebase Console con el identificador `com.example.semana13` y coloca el `google-services.json` en `android/app/`. El archivo está excluido de Git.
2. Abre `android/` con Android Studio, sincroniza Gradle y ejecuta la app en un dispositivo o emulador con Google Play Services.
3. Pulsa **Permitir notificaciones** cuando la app lo solicite.
4. Envía un mensaje de prueba desde Firebase Console. Para verificar `onMessageReceived`, prueba con la app abierta o con un mensaje de datos; con la app en segundo plano, Firebase puede mostrar directamente un mensaje que incluya `notification`.
5. Captura Logcat y la notificación real en el dispositivo. Este repositorio no incluye capturas fabricadas.

El proyecto requiere una instalación local de Android Studio/SDK y una configuración Firebase propia. Sin esas herramientas y credenciales no se puede generar ni validar un APK o una entrega push real.

## Git

Desde la raíz del proyecto:

```powershell
git switch -c feature/notificaciones
git add .
git commit -m "Agrega ejemplo de avisos y notificaciones FCM"
git push -u origin feature/notificaciones
```

Después abre un pull request, solicita revisión y haz merge a `main` cuando esté aprobado y probado.

## Alcance de las pruebas

Las pruebas Django validan que `GET /api/avisos/` responde `200` y JSON con los campos esperados. La integración Android/FCM debe configurarse y probarse en tu entorno antes de afirmar que el APK funciona.
