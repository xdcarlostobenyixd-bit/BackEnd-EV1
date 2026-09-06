from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    """
    Formulario basado en el modelo Contacto.
    Django valida automáticamente el formato del campo EmailField.
    """

    class Meta:
        model = Contacto
        fields = ["nombre", "telefono", "correo", "direccion"]
        labels = {
            "nombre": "Nombre",
            "telefono": "Teléfono",
            "correo": "Correo electrónico",
            "direccion": "Dirección",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Juan Pérez",
            }),
            "telefono": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: +56912345678",
            }),
            "correo": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: juan@correo.cl",
            }),
            "direccion": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Av. Principal 123",
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()

        # Estructura de decisión para evitar nombres vacíos.
        if not nombre:
            raise forms.ValidationError("El nombre no puede estar vacío.")

        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"].strip()

        # Validación simple: debe contener al menos 8 dígitos.
        digitos = sum(caracter.isdigit() for caracter in telefono)

        if digitos < 8:
            raise forms.ValidationError(
                "El teléfono debe contener al menos 8 dígitos."
            )

        return telefono
