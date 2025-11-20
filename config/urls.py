from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views  # Importamos nuestra vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # La ruta vacía '' es la portada
]

# Esto es necesario para poder ver las imágenes que subas mientras desarrollamos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)