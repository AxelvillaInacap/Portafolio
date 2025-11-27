from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        
        # Aquí le damos el estilo Apple/Minimalista a los inputs
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Tu Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'tu@correo.com'}),
            'asunto': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Asunto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Escribe tu mensaje aquí...', 'rows': 4}),
        }