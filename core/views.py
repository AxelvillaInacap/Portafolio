from django.shortcuts import render, redirect
from .models import Habilidad, Proyecto, Contacto, Trayectoria, Certificado
from .forms import MensajeForm

def home(request):
    # Lógica del Formulario
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigimos a la misma página con un parámetro de éxito
            return redirect('/?enviado=true#contacto')
    else:
        form = MensajeForm()

    # Datos para mostrar
    habilidades = Habilidad.objects.all()
    proyectos = Proyecto.objects.all()
    contactos = Contacto.objects.all()
    trayectoria = Trayectoria.objects.all()
    certificados = Certificado.objects.all()
    
    # Verificamos si el mensaje se envió con éxito (para mostrar alerta)
    mensaje_exito = request.GET.get('enviado') == 'true'

    context = {
        'habilidades': habilidades,
        'proyectos': proyectos,
        'contactos': contactos,
        'trayectoria': trayectoria,
        'certificados': certificados,
        'form': form,
        'mensaje_exito': mensaje_exito
    }

    return render(request, 'core/home.html', context)