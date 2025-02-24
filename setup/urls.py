"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api_ecommerce.api import viewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'categoria', viewsets.CategoriaViewSet)
route.register(r'produto', viewsets.ProdutoViewSet)
route.register(r'vendedor', viewsets.VendedorViewSet)
route.register(r'anuncio', viewsets.AnuncioViewSet)
route.register(r'recibo', viewsets.ReciboViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
