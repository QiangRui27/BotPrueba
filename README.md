# 📌 Bot de Telegram para Gestión de Leads con Dashboard en Django

## 1. Nombre del proyecto
**Bot de Telegram para Gestión de Leads con Dashboard en Django**  

## 2. Descripción
Este proyecto permite recopilar información de usuarios mediante un **bot de Telegram**, almacenar los datos en una base de datos y gestionarlos desde un **panel web (dashboard)**.  

Características principales:  
- Interacción paso a paso con los usuarios para recopilar: Nombre, Apellidos, Email, Teléfono y Dirección  
- Validación de datos (email y teléfono)  
- Confirmación de datos antes de guardarlos  
- Dashboard web para visualizar, editar y eliminar leads  
- Uso de ngrok para exponer el servidor local a Internet durante el desarrollo  

Desarrollado con **Python 3 y Django**, usando **Bootstrap** para la interfaz web y **Fetch API** para operaciones CRUD dinámicas.

## 3. Tecnologías utilizadas
- Python 3  
- Django  
- SQLite (desarrollo)  
- HTML, CSS, JavaScript  
- Bootstrap 5  
- Telegram Bot API  
- ngrok  

## 4. Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/QiangRui27/BotPrueba.git
cd <NOMBRE_DEL_PROYECTO>
```
2. Crear y activar un entorno virtual:

- Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
 - macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones
```bash
python manage.py migrate
```

5. Ejecutar el servidor

```bash
python manage.py runserver
```

## 5. Configuración del bot de Telegram

1. Crear un bot con BotFather y obtener el token.

2. Ejecutar ngrok para exponer el servidor local:
```bash
ngrok http 8000
```

3. Copiar la URL pública que genera ngrok (ej. https://abc123.ngrok-free.app)

4. Configurar el webhook de Telegram (terminal / cURL):
```bash
curl -X GET "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://abc123.ngrok-free.app/telegram/"
```

- Reemplazar <TOKEN> con tu token de bot.
- Asegúrate de que la ruta /telegram/ coincide con la de urls.py.

5. Verificar el webhook:

```bash
curl -X GET "https://api.telegram.org/bot<TOKEN>/getWebhookInfo"
```

## 6. Uso del Dashboard Web

1. Abrir el navegador en http://localhost:8000/
2. Visualizar métricas y últimos leads
3. Editar un lead con el botón ✏️ y guardar cambios
4. Eliminar un lead con el botón 🗑️ y confirmar
    
    >Las operaciones CRUD se realizan mediante Fetch API y modales de Bootstrap, sin recargar la página.

