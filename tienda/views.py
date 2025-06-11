from django.shortcuts import render, redirect

# Create your views here.
from .models import Producto
from .forms import ProductoForm, ClienteForm, BuscarProductoForm
from django.contrib import messages

def home(request):
    return render(request, 'base.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Producto guardado correctamente.")
                return redirect('home')
            else:
                messages.warning(request, "Formulario inválido. Revisá los datos ingresados.")
        except Exception as e:
            messages.error(request, f"Error inesperado al guardar el producto: {str(e)}")
    else:
        form = ProductoForm()
    
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Cliente agregado exitosamente.")
                return redirect('home')
            else:
                messages.error(request, "Formulario inválido. Verificá los datos ingresados.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error al guardar el cliente: {str(e)}")
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})

def buscar_producto(request):
    productos = []
    if request.method == 'GET':
        form = BuscarProductoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            productos = Producto.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarProductoForm()
    return render(request, 'buscar_producto.html', {'form': form, 'productos': productos})