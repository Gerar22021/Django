from django.db import models

# Create your models here.

class post(models.Model):
    nombre = models.CharField(max_length=20, null=False, unique=True)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='modulo1', default='categoria/imagen_default.png')
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    