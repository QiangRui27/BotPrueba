from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Author name: {self.name} - email: {self.email}"