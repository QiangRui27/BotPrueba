from django.db import models
from datetime import date

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField(default=3) # El campo score tendra un valor por defecto de 3 y es requerido
    comment = models.TextField(null=True) # El campo comment no es requerido
    date1 = models.DateTimeField(auto_now_add=True, null=True)
    date2 = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.name