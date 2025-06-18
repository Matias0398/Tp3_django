from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'home.html'
    context_object_name = 'productos'

class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto_list')
    success_message = "Producto creado correctamente."

class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto_list')
    success_message = "Producto actualizado correctamente."

class ProductoDeleteView(SuccessMessageMixin, DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
    success_message = "Producto eliminado correctamente."

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto/producto_detail.html'
    context_object_name = 'producto'

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    success_message = "Cliente creado exitosamente."

class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    success_message = "Cliente actualizado exitosamente."

class ClienteDeleteView(SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
    success_message = "Cliente eliminado exitosamente."

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/cliente_detail.html'
    context_object_name = 'cliente'
