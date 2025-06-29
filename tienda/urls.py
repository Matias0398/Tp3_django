from django.urls import path
from . import views

urlpatterns = [
    # URLs para Producto
    path('', views.ProductoListView.as_view(), name='producto_list'),
    path('producto/crear/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    
    # URLs para Cliente
    path('cliente/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('cliente/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    # URL para la vista about
    path('about/', views.about, name='about'),

    # URL para la vista de login
    path('login/', views.login_view, name='login'),

    # URL para la vista de logout
    path('logout/', views.logout_view, name='logout'),
]
