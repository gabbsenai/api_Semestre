from django.db import models

# Classe base com soft delete
class BaseModel(models.Model):
    ativo = models.BooleanField(default=True)

    def desativar(self):
        self.ativo = False
        self.save()

    class Meta:
        abstract = True

# Categoria
class Categoria(BaseModel):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Produto
class Produto(BaseModel):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')

    def __str__(self):
        return self.nome

# Vendedor
class Vendedor(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

# Anúncio
class Anuncio(BaseModel):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='anuncios')
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT, related_name='anuncios')
    data_anuncio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anúncio de {self.produto.nome} por {self.vendedor.nome}"

# Recibo
class Recibo(BaseModel):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.PROTECT, related_name='recibos')
    data_compra = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Recibo #{self.pk} - R$ {self.valor}"
