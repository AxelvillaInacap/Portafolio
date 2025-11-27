# Portafolio Profesional Dinámico (Django)

Este repositorio contiene el código fuente de mi portafolio web personal. Es una aplicación web desarrollada con **Django** que actúa como un CMS (Sistema de Gestión de Contenidos), permitiendo administrar toda la información (proyectos, habilidades, trayectoria, certificados) directamente desde un panel de administración, sin necesidad de modificar el código HTML.

## ✨ Características Principales

* **Diseño UI/UX Premium:** Estilo minimalista inspirado en la estética de Apple, con tipografía limpia, espaciado amplio y tarjetas con efectos de elevación.
* **Administración Total:** Todo el contenido es dinámico. Desde el panel `/admin` se pueden agregar, editar o eliminar:
    * Hitos de Trayectoria (Línea de tiempo).
    * Habilidades Técnicas (Barras de progreso).
    * Proyectos Destacados.
    * Certificaciones Académicas.
    * Redes de Contacto.
* **Formulario de Contacto Funcional:** Los mensajes enviados desde la web se guardan automáticamente en la base de datos para su gestión posterior.
* **Modo Oscuro (Dark Mode):** Detección automática de la preferencia del sistema y botón manual para alternar entre temas claro y oscuro, manteniendo la integridad del diseño.
* **Animaciones "Scroll Reveal":** Los elementos aparecen suavemente a medida que el usuario navega hacia abajo.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python, Django 5.x
* **Base de Datos:** SQLite 3 (Por defecto)
* **Frontend:** HTML5, CSS3 (Variables CSS, Flexbox, Grid), JavaScript Vanilla.
* **Librerías Adicionales:** `Pillow` (Manejo de imágenes).

## 🚀 Instalación y Ejecución Local

Si quieres probar este proyecto en tu máquina local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/AxelvillaInacap/Portafolio.git](https://github.com/AxelvillaInacap/Portafolio.git)
cd Portafolio
```

### 2. Configurar el Entorno Virtual
```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias y Preparar la Base de datos
```bash
pip install django Pillow
python manage.py migrate
```

### 4. Crear un superusuario
```bash
python manage.py createsuperuser
(Importante seguir las instrucciones del teminal)
```
### 5. Ejecutar el Servidor
```bash
python manage.py runserver
```


## ✨ Desarrollado por Axel Villa - Analista Programador