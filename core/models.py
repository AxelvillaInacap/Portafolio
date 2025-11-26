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