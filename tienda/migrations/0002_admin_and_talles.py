from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admin_and_talles(apps, schema_editor):
    Cliente = apps.get_model('tienda', 'Cliente')
    Talle = apps.get_model('tienda', 'Talle')
    # Crear usuario admin por defecto
    if not Cliente.objects.filter(email='admin@admin.com').exists():
        Cliente.objects.create(
            nombre='Administrador',
            email='admin@admin.com',
            telefono='123456789',
            password=make_password('admin123'),
            is_admin=True
        )
    # Crear talles por defecto
    talles = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
    for t in talles:
        Talle.objects.get_or_create(nombre=t)

def delete_admin_and_talles(apps, schema_editor):
    Cliente = apps.get_model('tienda', 'Cliente')
    Talle = apps.get_model('tienda', 'Talle')
    Cliente.objects.filter(email='admin@admin.com').delete()
    Talle.objects.filter(nombre__in=['XS', 'S', 'M', 'L', 'XL', 'XXL']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('tienda', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_admin_and_talles, delete_admin_and_talles),
    ]
