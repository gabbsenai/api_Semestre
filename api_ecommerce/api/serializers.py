from rest_framework import serializers
from api_ecommerce import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único da categoria'},
            'nome': {'help_text': 'Nome da categoria'},
            'descricao': {'help_text': 'Descrição detalhada da categoria'}
        }

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único do produto'},
            'nome': {'help_text': 'Nome do produto'},
            'descricao': {'help_text': 'Descrição detalhada do produto'},
            'categoria': {'help_text': 'Categoria a qual o produto pertence. Buscar no get de categorias'}
        }

class ProdutoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = ['nome', 'descricao', 'categoria']
        extra_kwargs = {
            'nome': {'help_text': 'Nome do produto'},
            'descricao': {'help_text': 'Descrição detalhada do produto'},
            'categoria': {'help_text': 'Categoria a qual o produto pertence. Buscar no get de categorias'}
        }

class AnuncioSerializer(serializers.ModelSerializer):
    produto = ProdutoNestedSerializer()

    class Meta:
        model = models.Anuncio
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único do anúncio'},
            'valor': {'help_text': 'Preço do produto no anúncio'},
            'descricao': {'help_text': 'Descrição do anúncio'},
            'vendedor': {'help_text': 'Vendedor responsável pelo anúncio (atribuição automática)', 'read_only': True},
            'quantidade': {'help_text': 'Quantidade disponível no anúncio'},
            'ativo': {'help_text': 'Indica se o anúncio está ativo ou inativo'}
        }

    def create(self, validated_data):
        produto_data = validated_data.pop('produto')
        vendedor_padrao = models.Vendedor.objects.first()
        if vendedor_padrao is None:
            raise serializers.ValidationError("Nenhum vendedor padrão foi encontrado no sistema.")
        
        produto = models.Produto.objects.create(vendedor=vendedor_padrao, **produto_data)
        anuncio = models.Anuncio.objects.create(produto=produto, vendedor=vendedor_padrao, **validated_data)
        return anuncio

class ReciboSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recibo
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único do recibo'},
            'anuncio': {'help_text': 'Anúncio relacionado ao recibo. Buscar no get de anuncio'},
            'vendedor': {'help_text': 'Vendedor responsável pela venda. Buscar no get de vendedor'},
            'descricao': {'help_text': 'Descrição da transação'},
            'data': {'help_text': 'Data da emissão do recibo'}
        }

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendedor
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador único do vendedor'},
            'nome': {'help_text': 'Nome do vendedor'},
            'email': {'help_text': 'Endereço de e-mail do vendedor'},
            'telefone': {'help_text': 'Número de telefone do vendedor'},
            'cpf': {'help_text': 'CPF do vendedor'},
            'endereco': {'help_text': 'Endereço completo do vendedor'},
            'descricao': {'help_text': 'Descrição sobre o vendedor'}
        }