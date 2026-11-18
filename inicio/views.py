import io
import base64
import matplotlib
matplotlib.use('Agg')  # Indispensable para Render (servidor sin pantalla)
import matplotlib.pyplot as plt

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

def graficas_view(request):
    error = None

    if request.method == 'POST':
        clave_ingresada = request.POST.get('clave', '')
        if clave_ingresada == '2110TXJ':  # Contraseña protegida
            request.session['acceso_graficas'] = True
            request.session.modified = True
            return redirect('graficas')  # Redirige por GET para evitar pantallas en blanco
        else:
            error = "Contraseña incorrecta. Intenta de nuevo."

    # 1. Verificar si ya ingresó la contraseña en esta sesión
    if not request.session.get('acceso_graficas', False):
        return render(request, 'login_graficas.html', {'error': error})

    # 2. Consultar los datos reales desde PostgreSQL usando tu modelo Resena
    c5 = Resena.objects.filter(calificacion=5).count()
    c4 = Resena.objects.filter(calificacion=4).count()
    c3 = Resena.objects.filter(calificacion=3).count()
    c2 = Resena.objects.filter(calificacion=2).count()
    c1 = Resena.objects.filter(calificacion=1).count()

    categorias = ['5 Estrellas', '4 Estrellas', '3 Estrellas', '2 Estrellas', '1 Estrella']
    cantidades = [c5, c4, c3, c2, c1]

    # 3. Dibujar la gráfica estadística con Matplotlib
    fig, ax = plt.subplots(figsize=(7, 4))
    barras = ax.bar(categorias, cantidades, color='#722F37', width=0.55)

    ax.set_title('Satisfacción de Clientes - Voces del Pasado', fontsize=13, fontweight='bold', pad=15)
    ax.set_ylabel('Cantidad de Evaluaciones')
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    for barra in barras:
        altura = barra.get_height()
        ax.annotate(f'{altura}',
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()

    # 4. Convertir la gráfica a Base64 para mostrarla en el HTML sin guardar archivos
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=120)
    buffer.seek(0)
    grafica_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close(fig)

    return render(request, 'graficas.html', {
        'grafica': grafica_base64,
        'total_registros': sum(cantidades),
    })
def logout_graficas(request):
    if 'acceso_graficas' in request.session:
        del request.session['acceso_graficas']
    return redirect('graficas')