# 🛍️ Mi Tienda Django

Este es un proyecto web de e-commerce básico desarrollado con Django y Python 3.13.4. El objetivo es gestionar productos y clientes, permitiendo la administración de un catálogo simple y la gestión de usuarios, incluyendo un sistema de login y registro personalizado.

## Explicación del proyecto

"Mi Tienda Django" es una aplicación web que simula una tienda online. Permite a los usuarios:
- Registrarse y autenticarse en la plataforma.
- Administrar productos (crear, listar, ver detalle, editar y eliminar) con nombre, descripción, precio y talle.
- Administrar clientes (crear, listar, ver detalle, editar y eliminar) con nombre, email y teléfono.
- Buscar productos por nombre.
- Navegar entre las diferentes secciones mediante un menú, sin necesidad de usar la barra de direcciones.
- Visualizar una página "About" con información sobre el creador del proyecto.

El sistema distingue entre usuarios normales y administradores. Solo los administradores pueden realizar operaciones CRUD completas sobre los modelos.

El diseño utiliza Bootstrap y herencia de plantillas para una experiencia visual moderna y responsiva.

## Modelos usados

- **Cliente**: almacena información de los usuarios registrados.
- **Producto**: almacena los productos disponibles en la tienda.
- **Talle**: almacena los diferentes talles disponibles para los productos.

## ¿Cómo probar el proyecto?

1. Clona el repositorio: `git clone 'url del repositorio'`
2. Activa el entorno virtual e instala los paquetes: `pip install -r requirements.txt`
3. Realiza las migraciones:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
4. Crea un superusuario para acceder al panel de administración: `python manage.py createsuperuser`
5. Inicia el servidor: `python manage.py runserver`
6. Accede a la app en `http://127.0.0.1:8000/` y al panel admin en `http://127.0.0.1:8000/admin/`
7. El programa carga por defecto un usuario tipo admin con correo:admin@admin.com y contraseña:admin123

## Curso
Comisión 75905
Profesor: Esteban H. Acevedo
[LinkedIn](linkedin.com/in/esteban-acevedo-aberastain)

## Alumno
Nombre: Matias Llanos
[LinkedIn](linkedin.com/in/matiasllanos98)