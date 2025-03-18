from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Anuncio

@api_view(["POST"])
def desativar_anuncio_api(request, anuncio_id):
    try:
        anuncio = Anuncio.objects.get(id=anuncio_id)
        anuncio.desativar()  # Chama o método de soft delete
        return Response({"success": True, "message": "Anúncio desativado com sucesso."})
    except Anuncio.DoesNotExist:
        return Response({"success": False, "message": "Anúncio não encontrado."}, status=404)
