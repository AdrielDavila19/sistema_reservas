from django.db import models

#aviao
class Aviao(models.Model): #define a classe Aviao que herda de models.Model
    identificacao = models.CharField(max_length=50, unique=True) #identificacao do avião, que deve ser único
    capacidade = models.IntegerField() #capacidade do avião
    fabricante = models.CharField(max_length=100) #fabricante do avião
    
        #__str__ é um método especial que define a instância do modelo que será representada como uma string
    def __str__(self): #def cria uma nova função ou metodo
        return self.identificacao #retorna a identificação do avião como string
    
#voo
class Voo(models.Model):
    aviao = models.ForeignKey(Aviao, on_delete=models.CASCADE) #chave estrangeira que referencia o modelo Aviao; on_delete=models.CASCADE garante que ao excluir uma instância de Aviao, todas as instâncias relacionadas de voo também serão excluídas
    origem = models.CharField(max_length=100) #origem do voo
    destino = models.CharField(max_length=100) #destino do voo 
    data = models.DateField() #data do voo
    horario = models.TimeField() #horário do voo
    
    def __str__(self):
        return f"{self.origem} para {self.destino} em {self.data} às {self.horario}" #retorna uma string formatada com origem, destino, data e horário do voo
    
#Cliente/pessoa
class Cliente(models.Model):
    nome = models.CharField(max_length=100) #nome do cliente
    cpf = models.CharField(max_length=11, unique=True) #CPF do cliente, que deve ser único
    telefone = models.CharField(max_length=15) #telefone do cliente
    email = models.CharField(max_length=100, unique=True) #email do cliente, que deve ser único
    
    def __str__(self):
        return self.nome #retorna o nome do cliente como string 
    
#Reserva
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #chave unica de cada cliente que referencia o modelo Cliente; on_delete=models.CASCADE garante que ao excluir uma instância de Cliente, todas as instâncias relacionadas de Reserva também serão excluídas
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE) #chave estrangeira que referencia o modelo Voo; on_delete=models.CASCADE garante que ao excluir uma instância de Voo, todas as instâncias relacionadas de Reserva também serão excluídas
    assento = models.CharField(max_length=10) #assento reservado pelo cliente
    
    class Meta: #Meta é uma classe interna, ja existente no django que define metadados para o modelo
        unique_together = ('cliente', 'voo', 'assento') #define que a combinação de cliente, voo e assento deve ser única, ou seja, um cliente não pode reservar o mesmo assento em um voo mais de uma vez 
    
    def __str__(self):
        return f"Reserva de {self.cliente} no voo {self.voo} - Assento: {self.assento}" #retorna uma string formatada com o cliente, voo e assento reservado   