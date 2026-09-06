from django.db import models


class Contacto(models.Model):
    # Datos principales solicitados por el Caso 3.
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=150)
    direccion = models.CharField(max_length=200)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
