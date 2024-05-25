# E-commerce API

Este é um projeto de API RESTful para gerenciamento de usuários, itens e pedidos, construído usando Django e Django Rest Framework.

## Funcionalidades

A API possui as seguintes funcionalidades:

### Gerenciamento de Usuários
- Criação de um novo usuário com um nome de usuário e senha exclusivos.
- Autenticação de um usuário usando nome de usuário e senha.
- Atualização das informações do perfil de um usuário (ex: nome, e-mail).
- Recuperação das informações do perfil de um usuário.

### Gerenciamento de Itens
- Criação de um novo item com nome e preço.
- Atualização do nome e preço de um item.
- Exclusão de um item.
- Recuperação de uma lista de todos os itens.

### Gestão de Pedidos
- Criação de um novo pedido para um usuário, contendo um ou vários itens.
- Recuperação de todos os pedidos de um usuário.
- Recuperação de detalhes de um pedido específico, incluindo os itens.

## Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

## Pré-requisitos

- Python 3.8+
- pip

## Instalação e Configuração

### 1. Clonando o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/Ianara-cs/ecommerce.git
cd ecommerce
```

### 2. Criando e Ativando um Ambiente Virtual
Crie e ative um ambiente virtual para o projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

### 3. Instalando as Dependências
Instale todas as dependências necessárias:

```bash
pip install -r requirements.txt
```
### 5. Executando as Migrações
Aplique as migrações do banco de dados para criar as tabelas necessárias:

```bash
python manage.py migrate
```
### 6. Criando um Superusuário
Crie um superusuário para acessar o admin do Django:

```bash
python manage.py createsuperuser
```

### 7. Executando o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

A API estará disponível em http://127.0.0.1:8000/.

A Documentação da API estará disponível em http://localhost:8000/swagger/