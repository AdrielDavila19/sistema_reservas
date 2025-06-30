# sistema_reservas
Este projeto é um estudo de Python com django para melhorar e implementar meu portifolio e habilidades como Dev. 

 Tem como objetivo ser um projeto real de resevas de voos, visando facilitar a vida de um possivel cliente, pegando uma necessidade e transformando em algo rapido e pratico em se executar.

  Usamos nesse projeto a definição "CRUD": Creat, Read, Update, Delet.

  # logo mais implementaremos o Front-end junto com o back, fazendo um projeto totalmente funcional.


# Passo a passo para instalação e para rodar o projeto.
# 1. Cria uma pasta e entra nela
mkdir projeto_voos
cd projeto_voos 

--------------------------------------------------------------------

# 2. Instala o Django
pip install django

--------------------------------------------------------------------

# 3. Cria o projeto
django-admin startproject sistema_reservas .

--------------------------------------------------------------------

# 4. Crie o app onde ficará a lógica
python manage.py startapp reservas

--------------------------------------------------------------------
////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////
-------------//----------------//-------------//--------------//----

Criar as tabelas no banco (migrações)

python manage.py makemigrations
python manage.py migrate

-----------------------------------

Criar superusuário para acessar o admin

python manage.py createsuperuser

Ele vai pedir:

Usuário

E-mail

Senha 

COMANDO PADRAO PARA RODAR O SERVIDOR: python manage.py runserver