from django.db import models

# Create your models here.

class Lead(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"