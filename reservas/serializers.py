from reservas.models import Aviao, Voo, Cliente, Reserva
from rest_framework import serializers

class AviaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aviao
        fields = ['identificacao', 'capacidade', 'fabricante']

class VooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voo
        fields = ['aviao', 'origem', 'destino', 'data', 'horario']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email']
        
class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ['cliente', 'voo', 'assento']
        