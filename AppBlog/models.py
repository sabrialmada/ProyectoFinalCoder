import email
from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=50, null=False)
    fecha = models.DateField(null=False)
    resenia = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.titulo+" "+str(self.autor)+" "+str(self.fecha)


class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.apellido)
