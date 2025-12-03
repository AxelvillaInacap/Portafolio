from django.db import models

# 1. TRAYECTORIA
class Trayectoria(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    lugar = models.CharField(max_length=100, verbose_name="Lugar")
    fecha = models.CharField(max_length=50, verbose_name="Fecha")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return f"{self.titulo} en {self.lugar}"

    class Meta:
        verbose_name = "Hito de Trayectoria"
        verbose_name_plural = "Trayectoria"
        ordering = ['-id']

# 2. HABILIDADES (MODIFICADO)
class Habilidad(models.Model):
    # Opciones para clasificar
    TIPOS = [
        ('BACK', 'Backend'),
        ('FRONT', 'Frontend'),
        ('OTHER', 'Herramientas / Otros'),
    ]
    
    nombre = models.CharField(max_length=50, verbose_name="Habilidad")
    nivel = models.IntegerField(default=50, verbose_name="Nivel (0-100)")
    # Nuevo campo 'tipo'
    tipo = models.CharField(max_length=5, choices=TIPOS, default='OTHER', verbose_name="Tipo")
    
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

# 3. PROYECTOS
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

# 4. CERTIFICADOS
class Certificado(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Nombre del Certificado")
    entidad = models.CharField(max_length=100, verbose_name="Institución")
    fecha = models.CharField(max_length=50, verbose_name="Fecha")
    imagen = models.ImageField(upload_to='certificados/', verbose_name="Imagen/Diploma", blank=True, null=True)
    link_credencial = models.URLField(blank=True, null=True, verbose_name="Link de Validación")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

# 5. CONTACTO (REDES)
class Contacto(models.Model):
    red = models.CharField(max_length=50, verbose_name="Red Social")
    url = models.URLField(verbose_name="Enlace")

    def __str__(self):
        return self.red

# 6. MENSAJES (FORMULARIO)
class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.nombre}: {self.asunto}"