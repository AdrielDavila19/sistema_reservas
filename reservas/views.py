from reservas.models import Aviao, Voo, Cliente, Reserva
from reservas.serializers import AviaoSerializer, VooSerializer, ClienteSerializer, ReservaSerializer
from rest_framework import viewsets

class AviaoViewSet(viewsets.ModelViewSet):
    queryset = Aviao.objects.all() # select identificacao, capacidade, fabricante from aviao
    serializer_class = AviaoSerializer

class VooViewSet(viewsets.ModelViewSet):
    queryset = Voo.objects.all() 
    serializer_class = VooSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer