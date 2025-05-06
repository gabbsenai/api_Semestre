from rest_framework import viewsets
from api_ecommerce.api import serializers
from api_ecommerce import models
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

# ------------------ CATEGORIA ------------------

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.filter(ativo=True)
    serializer_class = serializers.CategoriaSerializer

    @swagger_auto_schema(operation_description="Lista todas as categorias existentes")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cadastra uma categoria")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retorna a categoria conforme ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Edita os dados da categoria")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Desativa a categoria")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.desativar()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------ PRODUTO ------------------

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.filter(ativo=True)
    serializer_class = serializers.ProdutoSerializer

    @swagger_auto_schema(operation_description="Lista todos os produtos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cadastra um produto")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retorna o produto conforme ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Edita os dados do produto")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Desativa o produto")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.desativar()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------ VENDEDOR ------------------

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = models.Vendedor.objects.filter(ativo=True)
    serializer_class = serializers.VendedorSerializer

    @swagger_auto_schema(operation_description="Lista os vendedores")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cadastra um vendedor")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retorna o vendedor conforme ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Edita os dados do vendedor")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Desativa o vendedor")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.desativar()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------ ANUNCIO ------------------

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = models.Anuncio.objects.filter(ativo=True)
    serializer_class = serializers.AnuncioSerializer

    @swagger_auto_schema(operation_description="Lista todos os anúncios cadastrados")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cadastra um anúncio")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retorna o anúncio conforme ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Edita os dados do anúncio")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Desativa o anúncio")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.desativar()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------ RECIBO ------------------

class ReciboViewSet(viewsets.ModelViewSet):
    queryset = models.Recibo.objects.filter(ativo=True)
    serializer_class = serializers.ReciboSerializer

    @swagger_auto_schema(operation_description="Lista todos os recibos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cadastra um recibo")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retorna o recibo conforme ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Edita os dados do recibo")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Desativa o recibo")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.desativar()
        return Response(status=status.HTTP_204_NO_CONTENT)
