from django.db import models

class Reservacion(models.Model):
    OPCIONES_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de crédito'),
    ]

    nombre = models.CharField(max_length=120)
    numero = models.CharField(max_length=20)  # Teléfono de contacto
    metodo_pago = models.CharField(max_length=20, choices=OPCIONES_PAGO, default='efectivo')
    celebracion = models.CharField(max_length=100, blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Reserva de {self.nombre} - Tel: {self.numero}"

class Resena(models.Model):
    nombre = models.CharField(max_length=100)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Reseña de {self.nombre} ({self.calificacion} ★)"