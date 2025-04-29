# Django

## O que é

O **Django** é um framework web **Python** de código aberto, que se destaca por oferecer um ambiente que simplifica a criação de soluções web escaláveis, ao mesmo tempo, em que promove o desenvolvimento rápido e um design limpo, proporcionando ferramentas robustas e eficientes para pessoas desenvolvedoras.

Sendo uma das linguagens mais populares atualmente, [Python](https://www.alura.com.br/artigos/python-uma-introducao-a-linguagem)
 têm se destacado devido à sua sintaxe enxuta e simples, robustez e 
versatilidade. Amplamente adotada para o desenvolvimento de modelos de [machine learning](https://www.alura.com.br/artigos/machine-learning|), [inteligência artificial](https://www.alura.com.br/artigos/inteligencia-artificial-ia) e análise de dados, a linguagem também é utilizada para desenvolvimento de sistemas Web.

# Para que serve?

O Django é um framework que fornece um conjunto abrangente de ferramentas e componentes pré-construídos que **simplifica e acelera a criação de aplicações web robustas, escaláveis e seguras**.

Dadas suas características e facilidade de aplicação, este framework pode ser
 empregado em diversos contextos. Podemos citar alguns exemplos mais  conhecidos de utilização, tais como:

- **Criação de sites e aplicações web**: tendo sido projetado especificamente para essa
finalidade, com o Django é possível desenvolver desde simples sites informativos até sistemas complexos e interativos;
- **Plataformas de redes sociais**: diversas funcionalidades de redes sociais, como os
perfis de usuários, feeds de notícias e interações, podem ser implementadas com o Django. Alguns exemplos bastante conhecidos são o Instagram e o Pinterest;
- **Sistemas de gerenciamento interno**: diversas empresas utilizam o Django para criar ferramentas internas, como painéis de controles internos, sistemas de gerenciamento
de projetos, sistemas de rastreamento de logs, entre outras funcionalidades;
- **Aplicações e-commerce:** é possível utilizar o Django para construir plataformas robustas tendo em vista sua capacidade de gerenciar produtos, carrinhos de compras, pagamentos e
outros aspectos presentes em um comércio eletrônico;
- **Aplicações backend para aplicativos mobile**: é possível utilizar o Django para
desenvolver APIs que fornecem as funcionalidades backend para aplicativos Mobile.
- **Construção de APIs**: embora o Django seja mais comumente utilizado para a criação de sites e aplicações web, ele também fornece todas as ferramentas necessárias para criar APIs.

# Como funciona?

Uma das características que mais se destacam no Django é sua **arquitetura de design**, que utiliza a MVT (Model-View-Template). Essa abordagem é uma variação do tradicional padrão MVC (Model-View-Controller), amplamente adotada em diversos frameworks e sistemas, como Spring, ASP.NET, Express.js, entre outros.

# Componentes da arquitetura MVT

O padrão MVT divide o desenvolvimento web em três componentes principais: model, view e template.

## Estrutura de um Projeto Django

Um projeto Django é organizado de maneira a facilitar o desenvolvimento e a manutenção do código. Os principais componentes incluem:

### Arquivos Principais

- **`manage.py`**: Script para interagir com o projeto Django. Permite executar comandos como iniciar o servidor, criar migrações, entre outros.
- **`settings.py`**: Arquivo de configuração do projeto, onde são definidas as configurações do banco de dados, aplicativos instalados, middleware, entre outros.
- **`urls.py`**: Define as rotas do projeto, mapeando URLs para as respectivas views.
- **`wsgi.py`**: Ponto de entrada para servidores web. Permite que o projeto seja executado em servidores compatíveis com WSGI.

### Estrutura de Aplicativos

O Django é baseado no conceito de "aplicativos", que são componentes reutilizáveis dentro do projeto. Cada aplicativo contém:

- **`views.py`**: Define as views, que são responsáveis pela lógica de apresentação e processamento de dados.
- **`models.py`**: Define os modelos de dados, que representam as tabelas do banco de dados.
- **`urls.py`**: Define as rotas específicas do aplicativo, conectando URLs a views.
- **`templates/`**: Diretório que contém arquivos de template HTML usados para renderizar a interface do usuário.

## Criação de Views

As views são componentes essenciais em Django que processam as requisições do usuário e retornam respostas. Existem dois tipos principais de views:

### Function-Based Views (FBVs)

São funções que recebem uma solicitação e retornam uma resposta. Simples e diretas, ideais para casos onde a lógica não é complexa.

Exemplo:

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

```

### Class-Based Views (CBVs)

Permitem uma estrutura mais orientada a objetos, facilitando a reutilização e a extensão da lógica de views. Utilizam herança para criar diferentes tipos de views com base em classes base do Django.

Exemplo:

```python
from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")

```

### Criação de URLs para Views

As URLs são definidas no arquivo `urls.py`, onde você pode associar uma URL a uma view específica.

Exemplo de configuração de URLs:

```python
from django.urls import path
from .views import lista_de_livros

urlpatterns = [
    path('livros/', lista_de_livros, name='lista_de_livros'),
]

```

## Modelos e Migrations

### Criação de Modelos

Os modelos são definidos em `models.py` e representam a estrutura dos dados, incluindo campos e tipos de dados. Cada modelo é mapeado para uma tabela no banco de dados.

### Definição de Campos e Tipos de Dados

Django oferece uma variedade de campos para criar modelos, como `CharField`, `TextField`, `DecimalField`, entre outros. Cada campo tem parâmetros que definem seu comportamento.

### Geração e Aplicação de Migrations

Migrations são usadas para criar ou modificar tabelas no banco de dados. Você pode gerar migrations automaticamente a partir dos modelos usando o comando:

```bash
python manage.py makemigrations
```

E aplicar as migrations com:

```bash
python manage.py migrate
```

## Template

Django utiliza templates para gerar HTML dinâmico, combinando partes estáticas e sintaxe para conteúdo dinâmico. Abaixo estão os principais conceitos relacionados aos templates.

### Configuração e Motores de Template

- O Django suporta seu próprio sistema de templates (Django Template Language - DTL) e Jinja2.
- É possível usar múltiplos motores de template ou nenhum, dependendo das necessidades do projeto.

### Django Template Language (DTL)

O DTL é recomendado para aplicações que distribuem templates, como o painel administrativo do Django. Cuidado ao permitir que usuários não confiáveis criem templates, pois isso pode levar a vulnerabilidades de segurança, como ataques XSS.

### Sintaxe do Django Template Language

### Elementos da Sintaxe

1. **Variáveis**
    - Sintaxe: `{{ variavel }}`
    - Exemplo: `Meu nome é {{ first_name }} {{ last_name }}` renderiza como "Meu nome é John Doe" se o contexto for `{'first_name': 'John', 'last_name': 'Doe'}`.
2. **Tags**
    - Sintaxe: `{% tag %}`
    - Exemplo: `{% if user.is_authenticated %}Olá, {{ user.username }}.{% endif %}`.
3. **Filtros**
    - Sintaxe: `{{ variavel|filtro }}`
    - Exemplo: `{{ django|title }}` resulta em "The Web Framework For Perfectionists With Deadlines".
4. **Comentários**
    - Sintaxe: `{# Este é um comentário #}`

Essa estrutura fornece uma visão clara sobre como um projeto Django é organizado e como as diferentes partes interagem entre si para formar uma aplicação web robusta.

### Materiais de Referência

- Documentação do [Django Project](https://docs.djangoproject.com/)
- [https://www.alura.com.br/artigos/django-framework](https://www.alura.com.br/artigos/django-framework)
