from django.shortcuts import render, redirect
from .forms import ReservacionForm
from .models import Resena  # <--- Importante: Importar el modelo de Reseña

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def platillos(request):
    return render(request, 'platillos.html')

def menu_pdf(request):
    return render(request, 'menu_pdf.html')

def ubicacion(request):
    return render(request, 'ubicacion.html')

def vista_reservaciones(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda las reservaciones directo en PostgreSQL
            return redirect('inicio')
    else:
        form = ReservacionForm()
    
    return render(request, 'reservaciones.html', {'form': form})

def resenas(request):
    if request.method == 'POST':
        # Captura los datos enviados desde tu formulario HTML de reseñas
        nombre = request.POST.get('nombre')
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')
        
        # Guarda la reseña en la base de datos para que aparezca en el Admin
        if nombre and calificacion and comentario:
            Resena.objects.create(
                nombre=nombre,
                calificacion=calificacion,
                comentario=comentario
            )
        return redirect('resenas')
    
    # Trae todas las reseñas de la base de datos (ordenadas de la más nueva a la más antigua)
    lista_resenas = Resena.objects.all().order_by('-creado_en')
    
    return render(request, 'resenas.html', {'resenas': lista_resenas})