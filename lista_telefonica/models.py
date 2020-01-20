from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    nome = models.CharField(max_length=255)   
    descricao = models.CharField(max_length=255)
    telefone = models.CharField(max_length=14)
    valor = models.DecimalField(max_digits=9, decimal_places=2, null= True)

    def __str__(self):
        return self.nome