from django.shortcuts import render, redirect

# Create your views here.
from .models import Producto
from .forms import ProductoForm, ClienteForm, BuscarProductoForm

def home(request):
    return render(request, 'base.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
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