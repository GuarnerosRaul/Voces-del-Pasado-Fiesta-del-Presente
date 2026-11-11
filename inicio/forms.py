from django import forms
from .models import Reservacion, Resena

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['nombre', 'numero', 'metodo_pago', 'celebracion', 'alergias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre completo'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono (10 dígitos)'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
            'celebracion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Cumpleaños, Aniversario (Opcional)'}),
            'alergias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '¿Tienes alguna alergia o restricción alimentaria?'}),
        }

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['nombre', 'calificacion', 'comentario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'calificacion': forms.Select(attrs={
                'class': 'form-select',
            }, choices=[
                (5, '★★★★★ - Excelente'),
                (4, '★★★★☆ - Muy Buena'),
                (3, '★★★☆☆ - Buena'),
                (2, '★★☆☆☆ - Regular'),
                (1, '★☆☆☆☆ - Mala'),
            ]),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Platícanos tu experiencia...'}),
        }