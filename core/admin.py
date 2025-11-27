from django.contrib import admin
from .models import Habilidad, Proyecto, Contacto, Mensaje, Trayectoria, Certificado

admin.site.register(Habilidad)
admin.site.register(Proyecto)
admin.site.register(Contacto)
admin.site.register(Trayectoria)
admin.site.register(Certificado)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto')
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'fecha_envio')