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
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from api_ecommerce.views import desativar_anuncio_api
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="Sistema para controle do ecommerce",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@doador.com.br"),
        license=openapi.License(name="Free"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

route = routers.DefaultRouter()
route.register(r'categoria', viewsets.CategoriaViewSet)
route.register(r'produto', viewsets.ProdutoViewSet)
route.register(r'vendedor', viewsets.VendedorViewSet)
route.register(r'anuncio', viewsets.AnuncioViewSet)
route.register(r'recibo', viewsets.ReciboViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path("anuncio/<int:anuncio_id>/desativar/", desativar_anuncio_api, name="desativar_anuncio"),
]
urlpatterns += [
    path('swaggerjson', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)