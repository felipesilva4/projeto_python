from django.db import models

# Create your models here.
class Vitimas1(models.Model):
    nome= models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=60)
    telefone = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=16)
