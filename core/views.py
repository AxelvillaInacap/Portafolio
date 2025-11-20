from django.shortcuts import render
from .models import Habilidad, Proyecto, Contacto

def home(request):
    # 1. Traemos todos los datos de la base de datos
    habilidades = Habilidad.objects.all()
    proyectos = Proyecto.objects.all()
    contactos = Contacto.objects.all()

    # 2. Los empaquetamos en un diccionario "contexto"
    context = {
        'habilidades': habilidades,
        'proyectos': proyectos,
        'contactos': contactos,
    }

    # 3. Enviamos ese paquete al archivo HTML (que crearemos pronto)
    return render(request, 'core/home.html', context)