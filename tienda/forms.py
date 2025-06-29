from django import forms
from .models import Producto, Cliente
from django.contrib.auth.hashers import make_password

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'talle']

class ClienteForm(forms.ModelForm):
    password2 = forms.CharField(
        label='Confirme su contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña'
        })
    )
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'password']
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
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña'
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
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        instance.is_admin = False
        if commit:
            instance.save()
        return instance
