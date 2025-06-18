from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'talle']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'password', 'password2']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo electrónico'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su número de teléfono'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña'
            }),
            'password2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirme su contraseña'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if not password:
            raise forms.ValidationError('La contraseña es obligatoria')
        
        if not password2:
            raise forms.ValidationError('Debes confirmar la contraseña')

        if password and password2 and password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
