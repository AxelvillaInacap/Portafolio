from django.db import models

# 1. Modelo para tus Habilidades
class Habilidad(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Habilidad")
    nivel = models.IntegerField(default=50, verbose_name="Nivel (0-100)") 
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

# 2. Modelo para tus Proyectos
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    link_github = models.URLField(blank=True, null=True, verbose_name="Link GitHub")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

# 3. Modelo para Contacto
class Contacto(models.Model):
    red = models.CharField(max_length=50, verbose_name="Red Social (Ej: LinkedIn)")
    url = models.URLField(verbose_name="Enlace")

    def __str__(self):
        return self.red
    
class Mensaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.asunto}"

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes Recibidos"
        ordering = ['-fecha_envio'] # Los más nuevos primero

# NUEVO MODELO: Trayectoria (Timeline)
class Trayectoria(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título (Puesto/Carrera)")
    lugar = models.CharField(max_length=100, verbose_name="Lugar (Empresa/Institución)")
    fecha = models.CharField(max_length=50, verbose_name="Fecha (Ej: 2023 - Presente)")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción breve")

    def __str__(self):
        return f"{self.titulo} en {self.lugar}"

    class Meta:
        verbose_name = "Hito de Trayectoria"
        verbose_name_plural = "Trayectoria"
        ordering = ['-id'] # Los últimos que agregues saldrán primero (arriba)

class Certificado(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Nombre del Certificado")
    entidad = models.CharField(max_length=100, verbose_name="Institución (Ej: INACAP)")
    fecha = models.CharField(max_length=50, verbose_name="Fecha de obtención")
    # Opcional: Una foto del diploma para mostrarlo
    imagen = models.ImageField(upload_to='certificados/', verbose_name="Imagen/Diploma", blank=True, null=True)
    # Opcional: Link a credencial digital (si tienes)
    link_credencial = models.URLField(blank=True, null=True, verbose_name="Link de Validación")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"