from django.db import models
import os
import uuid
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return self.nome

@deconstructible
class RenameImage(object):
    def __init__(self, subdir='images'):
        self.subdir = subdir

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        new_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join(self.subdir, new_name)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey('Vendedor', on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to=RenameImage('images'), blank=True, null=True)

    def __str__(self):
        
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    endereco = models.TextField(max_length=150)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=255)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True, null=False)

    def desativar(self):
        """Desativa o anúncio em vez de removê-lo fisicamente."""
        self.ativo = False
        self.save()

    def delete(self, *args, **kwargs):
        """Override do delete para realizar o soft delete."""
        self.desativar()

    def __str__(self):
        return f"{self.produto.nome} - R$ {self.valor}"

class Recibo(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.DO_NOTHING)
    descricao = models.TextField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f"Recibo de {self.anuncio.produto.nome} - {self.data}"