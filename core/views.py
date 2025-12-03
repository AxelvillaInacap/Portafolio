from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Habilidad, Proyecto, Contacto, Mensaje, Trayectoria, Certificado
from .forms import MensajeForm

def home(request):
    # Lógica del Formulario
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje_nuevo = form.save()
            
            # Enviar correo (Opcional, si tienes configurado settings.py)
            try:
                subject = f"Nuevo mensaje: {mensaje_nuevo.asunto}"
                body = f"De: {mensaje_nuevo.nombre}\nCorreo: {mensaje_nuevo.email}\n\n{mensaje_nuevo.mensaje}"
                send_mail(subject, body, settings.EMAIL_HOST_USER, ['axelmatiasvilla1@gmail.com'], fail_silently=True)
            except:
                pass # Si falla el correo, no rompemos la página

            return redirect('/?enviado=true#contacto')
    else:
        form = MensajeForm()

    # Consultas a la BD
    # AQUÍ SEPARAMOS LAS HABILIDADES
    habilidades_back = Habilidad.objects.filter(tipo='BACK')
    habilidades_front = Habilidad.objects.filter(tipo='FRONT')
    habilidades_other = Habilidad.objects.filter(tipo='OTHER')

    proyectos = Proyecto.objects.all()
    contactos = Contacto.objects.all()
    trayectoria = Trayectoria.objects.all()
    certificados = Certificado.objects.all()
    
    mensaje_exito = request.GET.get('enviado') == 'true'

    context = {
        'habilidades_back': habilidades_back,
        'habilidades_front': habilidades_front,
        'habilidades_other': habilidades_other,
        'proyectos': proyectos,
        'contactos': contactos,
        'trayectoria': trayectoria,
        'certificados': certificados,
        'form': form,
        'mensaje_exito': mensaje_exito
    }

    return render(request, 'core/home.html', context)