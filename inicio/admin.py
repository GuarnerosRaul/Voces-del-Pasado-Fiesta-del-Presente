from django.contrib import admin
from .models import Reservacion, Resena

@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'metodo_pago', 'celebracion', 'creado_en')
    search_fields = ('nombre', 'numero')

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion', 'creado_en')
    search_fields = ('nombre', 'comentario')

# Register your models here.