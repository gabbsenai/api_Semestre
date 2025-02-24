from rest_framework import serializers
from api_ecommerce import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = '__all__'

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anuncio
        fields = '__all__'  

class ReciboSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recibo
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendedor
        fields = '__all__'
