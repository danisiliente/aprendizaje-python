from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    contrasenha = models.CharField(max_length=100, verbose_name='Contrasenha')
    