from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
from django.contrib.auth.hashers import check_password

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'home.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto_list')
    success_message = "Producto creado correctamente."

    def dispatch(self, request, *args, **kwargs):
        cliente_id = request.session.get('cliente_id')
        if not cliente_id:
            messages.error(request, 'Debes iniciar sesión como administrador para acceder a esta página.')
            return redirect('login')
        from .models import Cliente
        cliente = Cliente.objects.filter(id=cliente_id, is_admin=True).first()
        if not cliente:
            messages.error(request, 'No tienes permisos para crear productos. Solo el administrador puede acceder.')
            return redirect('producto_list')
        return super().dispatch(request, *args, **kwargs)

class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto_list')
    success_message = "Producto actualizado correctamente."

    def dispatch(self, request, *args, **kwargs):
        cliente_id = request.session.get('cliente_id')
        if not cliente_id:
            messages.error(request, 'Debes iniciar sesión como administrador para acceder a esta página.')
            return redirect('login')
        from .models import Cliente
        cliente = Cliente.objects.filter(id=cliente_id, is_admin=True).first()
        if not cliente:
            messages.error(request, 'No tienes permisos para editar productos. Solo el administrador puede acceder.')
            return redirect('producto_list')
        return super().dispatch(request, *args, **kwargs)

class ProductoDeleteView(SuccessMessageMixin, DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
    success_message = "Producto eliminado correctamente."

    def dispatch(self, request, *args, **kwargs):
        cliente_id = request.session.get('cliente_id')
        if not cliente_id:
            messages.error(request, 'Debes iniciar sesión como administrador para acceder a esta página.')
            return redirect('login')
        from .models import Cliente
        cliente = Cliente.objects.filter(id=cliente_id, is_admin=True).first()
        if not cliente:
            messages.error(request, 'No tienes permisos para eliminar productos. Solo el administrador puede acceder.')
            return redirect('producto_list')
        return super().dispatch(request, *args, **kwargs)

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto/producto_detail.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente_id = self.request.session.get('cliente_id')
        es_admin = False
        if cliente_id:
            cliente = Cliente.objects.filter(id=cliente_id).first()
            if cliente and cliente.is_admin:
                es_admin = True
        context['es_admin'] = es_admin
        return context

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('producto_list')  # Redirige al inicio tras registrarse
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

def about(request):
    return render(request, 'about/about.html', {
        'autor': 'Matías',
        'descripcion': 'Proyecto Django realizado para la materia Programación. Incluye gestión de productos y clientes.'
    })

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            cliente = Cliente.objects.get(email=email)
            if check_password(password, cliente.password):
                request.session['cliente_id'] = cliente.id
                request.session['cliente_nombre'] = cliente.nombre
                request.session['cliente_email'] = cliente.email
                return redirect('producto_list')
            else:
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        except Cliente.DoesNotExist:
            return redirect('cliente_create')
    return render(request, 'login.html')

def logout_view(request):
    try:
        del request.session['cliente_id']
    except KeyError:
        pass
    return redirect('login')
