from rest_framework import viewsets
from api_ecommerce.api import serializers
from api_ecommerce import models
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    @swagger_auto_schema(
        operation_description="Lista todas as categorias existentes",
        responses={200: serializers.CategoriaSerializer(many=True)}
    ) #decorador para descrição do método
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cadastra uma categoria",
        responses={201: "Nova categoria cadastrado"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_description="Retorna a categoria conforme ID",
            responses={200: "Categoria encontrada encontrado"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Edita os dados da categoria",
        responses={200: "Categoria atualizado"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Excluí a categoria",
        responses={204: "Categoria excluída"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    @swagger_auto_schema(
        operation_description="Lista todos os produtos",
        responses={200: serializers.ProdutoSerializer(many=True)}
    ) #decorador para descrição do método
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cadastra um produto",
        responses={201: "Novo produto cadastrado"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_description="Retorna o produto conforme ID",
            responses={200: "Produto encontrado"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Edita os dados do produto",
        responses={200: "Produto atualizado"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Excluí o produto",
        responses={204: "Produto excluído"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = models.Vendedor.objects.all()
    serializer_class = serializers.VendedorSerializer
    @swagger_auto_schema(
        operation_description="Lista os vendedores",
        responses={200: serializers.VendedorSerializer(many=True)}
    ) #decorador para descrição do método
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cadastra um vendedor",
        responses={201: "Novo vendedor cadastrado"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_description="Retorna o vendedor conforme ID",
            responses={200: "Vendedor encontrado"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Edita os dados do vendedor",
        responses={200: "Dados do vendedor atualizados"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Excluí o vendedor",
        responses={204: "Vendedor excluído"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = models.Anuncio.objects.filter(ativo=True)
    serializer_class = serializers.AnuncioSerializer

    @swagger_auto_schema(
        operation_description="Lista todos os anúncios cadastrados",
        responses={200: serializers.AnuncioSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cadastra um anúncio",
        responses={201: "Novo anúncio cadastrado"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna o anúncio conforme ID",
        responses={200: "Anúncio encontrado"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Edita os dados do anúncio",
        responses={200: "Anúncio atualizado"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Excluí o anúncio (soft delete)",
        responses={204: "Anúncio desativado"}
    )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.desativar()  # Realiza o soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReciboViewSet(viewsets.ModelViewSet):
    queryset = models.Recibo.objects.all()
    serializer_class = serializers.ReciboSerializer
    @swagger_auto_schema(
        operation_description="Lista todos os recibos",
        responses={200: serializers.ReciboSerializer(many=True)}
    ) #decorador para descrição do método
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cadastra um recibo",
        responses={201: "Novo recibo cadastrado"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_description="Retorna o recibo conforme ID",
            responses={200: "Recibo encontrado"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Edita os dados do recibo",
        responses={200: "Recibo atualizado"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Excluí o recibo",
        responses={204: "Recibo excluído"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)