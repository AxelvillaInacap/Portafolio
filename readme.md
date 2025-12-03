# Portafolio Profesional Dinámico (Django)

Este repositorio contiene el código fuente de mi portafolio web personal. Es una aplicación web desarrollada con **Django** que actúa como un CMS (Sistema de Gestión de Contenidos), permitiendo administrar toda la información (proyectos, habilidades, trayectoria, certificados) directamente desde un panel de administración, sin necesidad de tocar el código.

## ✨ Características Principales

* **Diseño UI/UX Premium:** Estilo minimalista inspirado en la estética de Apple, con tipografía limpia, espaciado amplio y tarjetas con efectos de elevación ("Glassmorphism").
* **Administración Total:** Todo el contenido es dinámico. Desde el panel `/admin` se pueden gestionar:
    * **Trayectoria:** Línea de tiempo cronológica (Educación y Experiencia).
    * **Habilidades:** Barras de progreso divididas en Backend y Frontend.
    * **Proyectos:** Tarjetas con descripciones y enlaces a repositorios.
    * **Certificaciones:** Sección dedicada para diplomas y credenciales.
    * **Redes de Contacto:** Enlaces a plataformas sociales.
* **Formulario de Contacto Funcional:** Los mensajes enviados desde la web se guardan en la base de datos y **envían una notificación automática por correo electrónico** (SMTP) al administrador.
* **Modo Oscuro (Dark Mode):** Detección automática de la preferencia del sistema y botón manual para alternar entre temas claro y oscuro.
* **Animaciones:** Efecto "Scroll Reveal" para una experiencia de navegación fluida.
* **Seguridad:** Uso de variables de entorno para proteger credenciales sensibles.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x, Django 5.x
* **Base de Datos:** SQLite 3 (Por defecto)
* **Frontend:** HTML5, CSS3 (Variables CSS, Flexbox, Grid), JavaScript Vanilla.
* **Librerías Clave:**
    * `Pillow` (Manejo de imágenes).
    * `python-dotenv` (Seguridad y Variables de Entorno).

---

## 🚀 Instalación y Ejecución Local

Sigue estos pasos exactos para levantar el proyecto en tu máquina:

### 1. Clonar el Repositorio
```bash
git clone [https://github.com/AxelvillaInacap/Portafolio.git](https://github.com/AxelvillaInacap/Portafolio.git)
cd Portafolio
```

### 2. Configurar entorno virtual
```bash
# Crear el venv
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install django Pillow python-dotenv
```

### 4. Configurar Variables de entorno (IMPORTANTE)
```bash
EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion

# nota: La contraseña debe ser una "Contraseña de Aplicación" de Google de 16 caracteres, no tu clave habitual
```

### 5. Preparar la base de datos

```bash
python manage.py migrate
```

### 6. Crear un SuperUsuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor
```bash
python manage.py runserver
```
---------------------------------------------

## Como Probar la aplicacion
Ver el Portafolio: Abre http://127.0.0.1:8000/.

Panel de Administración: Ve a http://127.0.0.1:8000/admin/ e inicia sesión.

Aquí podrás crear, editar y eliminar tus Proyectos, Habilidades, Certificados y Trayectoria.

Probar Contacto: Llena el formulario al final de la página principal. Si el archivo .env está correcto, recibirás un correo electrónico real.

# Desarrollado Por Axel Villa