from django.contrib import admin # importa o módulo admin do Django para registrar modelos no site de administração
from .models import Aviao, Voo, Cliente, Reserva #importa os modelos Aviao, Voo, Cliente e Reserva

#Registro: Adriel_Davila / senha: 123456

admin.site.register(Aviao) #registra o modelo Aviao no site de administração do Django
admin.site.register(Voo) #registra o modelo Voo no site de administração do Django
admin.site.register(Cliente) #registra o modelo Cliente no site de administração do Django
admin.site.register(Reserva) #registra o modelo Reserva no site de administração do Django

