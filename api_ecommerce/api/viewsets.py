from rest_framework import viewsets
from api_ecommerce.api import serializers
from api_ecommerce import models

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = models.Vendedor.objects.all()
    serializer_class = serializers.VendedorSerializer

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = models.Anuncio.objects.all()
    serializer_class = serializers.AnuncioSerializer

class ReciboViewSet(viewsets.ModelViewSet):
    queryset = models.Recibo.objects.all()
    serializer_class = serializers.ReciboSerializer