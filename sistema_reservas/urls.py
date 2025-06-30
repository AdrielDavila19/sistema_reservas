from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservas.views import AviaoViewSet, VooViewSet, ClienteViewSet, ReservaViewSet


# Criar o roteador e registrar as ViewSets
router = DefaultRouter()
router.register(r'avioes', AviaoViewSet)
router.register(r'voos', VooViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)

# Inclui as rotas geradas automaticamente pelo DRF
urlpatterns = [
    path('api/', include(router.urls)),]