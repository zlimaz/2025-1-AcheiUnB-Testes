## O que é Django REST Framework?

O Django REST Framework (DRF) é uma biblioteca poderosa e flexível, construída sobre o Django, que facilita a criação de APIs Web RESTful. Ele oferece ferramentas para desenvolvedores construírem APIs robustas e escaláveis para suas aplicações.

Para estudarmos Django API Rest precisamos primeiro definir conceitos para o entendimento geral.

## API

A API (Application Programming Interface) é um conjunto de regras e definições que tem como função intermediar a comunicação universal entre diferentes sistemas Em outras palavras, é uma interface que possibilita que um sistema utilize funcionalidades de outro sistema sem precisar entender sua implementação interna. 

## Rest

Rest (Representational State Transfer) é um estilo arquitetural usado para construir APIs que permitem a comunicação entre sistemas através do protocolo HTTP. APIs que seguem este estilo são conhecidas como **APIs RESTful**. Elas se baseiam em um conjunto de princípios que tornam as comunicações leves, escaláveis e fáceis de manter.

Rest tem como principais conceitos:

- **Recursos**:
    - Em REST, qualquer entidade ou dado manipulável é chamado de **recurso**. Por exemplo, em um sistema de gestão de usuários, "usuário" seria um recurso.
    - Cada recurso é representado por uma **URL única** (endpoint), como `/usuarios/1` para o usuário com ID 1.
- **Métodos HTTP**:
    - As operações sobre recursos são realizadas por meio dos métodos HTTP. Os mais comuns são:
        - **GET**: Para ler ou recuperar um recurso.
        - **POST**: Para criar um novo recurso.
        - **PUT**: Para atualizar um recurso existente.
        - **DELETE**: Para deletar um recurso.
- **Representação de recursos**:
    - Os recursos são transferidos entre cliente e servidor em formatos padronizados, como **JSON** ou **XML**, facilitando a comunicação.
- **Sem estado (stateless)**:
    - Em REST, cada solicitação do cliente ao servidor deve conter todas as informações necessárias para ser compreendida e processada. O servidor não mantém o estado da sessão entre as requisições.
- **Cacheabilidade**:
    - Respostas HTTP podem ser configuradas como cacheáveis, permitindo que os clientes armazenem respostas temporariamente, o que melhora a eficiência e reduz a carga no servidor.
- **Sistema em camadas**:
    - Em uma arquitetura REST, componentes intermediários, como proxies e gateways, podem ser inseridos para melhorar a escalabilidade e segurança, sem que o cliente ou servidor precise se adaptar.

## Serialização

No Django REST Framework (DRF), **serialização** é o processo de converter dados complexos, como objetos de modelos Django, em formatos que possam ser facilmente compartilhados entre sistemas, geralmente **JSON** ou **XML**.

 Isso permite que esses dados sejam enviados como respostas de uma API e compreendidos por clientes, como navegadores e aplicativos móveis. A serialização também funciona no sentido inverso, permitindo que dados recebidos (em JSON, por exemplo) sejam convertidos em objetos do Django para serem armazenados no banco de dados.

![DRF_Serialização](https://github.com/user-attachments/assets/f0f95c6a-b05e-4c2b-927e-21fd4b8316f9)

## Segurança no DRF (Django Rest Framework)

### 1. **Autenticação**

- DRF suporta vários métodos de autenticação que garantem que apenas usuários autorizados possam acessar certos endpoints.
- **Token Authentication**: Gera um token exclusivo para cada usuário que é enviado em cada requisição, geralmente no cabeçalho de autorização.
- **Session Authentication**: Usa sessões do Django para autenticar o usuário, ideal para APIs que serão acessadas a partir de uma aplicação web do Django.
- **JWT (JSON Web Tokens)**: JWT é uma forma popular e segura de autenticação que permite que um token assinado seja passado entre cliente e servidor.
- **OAuth2**: DRF também pode ser integrado ao OAuth2 para permitir autenticação segura e autorização em plataformas de terceiros, como Google ou Facebook.

### 2. **Autorização**

- **Permissions**: DRF permite configurar permissões de acesso para cada endpoint, definindo regras sobre quem pode acessar ou modificar os dados.
    - **AllowAny**: Permite acesso a qualquer usuário.
    - **IsAuthenticated**: Permite apenas usuários autenticados.
    - **IsAdminUser**: Restringe o acesso a usuários com status de administrador.
    - **IsAuthenticatedOrReadOnly**: Permite acesso total a usuários autenticados e apenas leitura para não autenticados.
- **Permissões personalizadas**: DRF permite criar regras específicas, como permitir o acesso apenas ao proprietário de um recurso.

### 3. **Throttle (Limite de Requisições)**

- **Throttle** (ou rate limiting) controla o número de requisições que um usuário pode fazer em um determinado período de tempo.
- Isso ajuda a evitar ataques de força bruta, como tentativas de login em massa ou sobrecarga do sistema.
- DRF oferece throttles de escopo por usuário, anônimo ou global, que podem ser personalizados.

### 4. **Validação de Dados**

- O DRF fornece ferramentas robustas de validação para impedir que dados mal formatados ou não confiáveis sejam processados.
- A validação é feita automaticamente com base nos serializers, e regras personalizadas podem ser adicionadas conforme necessário.

### 5. **Proteção Contra Cross-Site Scripting (XSS) e Injeção de SQL**

- DRF herda as proteções contra XSS e injeção de SQL do Django. As consultas ao banco de dados são parametrizadas, o que evita que dados inseridos pelo usuário modifiquem a estrutura das consultas SQL.
- Para XSS, o Django realiza uma sanitização automática de dados exibidos em templates HTML, protegendo a aplicação contra scripts maliciosos.

### 6. **Criptografia e HTTPS**

- Embora não seja exclusivo do DRF, é fundamental que APIs sejam acessadas apenas por **HTTPS** para garantir a criptografia dos dados transmitidos.
- O DRF facilita o uso de headers e configurações de segurança, mas a criptografia é uma configuração a ser feita no nível do servidor.

### 7. **Proteção Contra Exposição de Informações Sensíveis**

- É importante garantir que dados sensíveis, como senhas, tokens de API e detalhes de autenticação, sejam adequadamente protegidos.
- DRF permite definir quais campos serão exibidos em respostas usando serializers e fornece métodos para garantir que dados sensíveis não sejam expostos.

### 8. **Logs e Monitoramento de Segurança**

- DRF permite que você monitore e registre atividades, o que é útil para identificar e responder a acessos ou tentativas de acessos suspeitos.

## Instalação

Você pode instalar o Django REST Framework usando o `pip`, incluindo quaisquer pacotes opcionais que desejar:

```bash
pip install djangorestframework
pip install markdown       # Suporte a Markdown para a API navegável.
pip install django-filter  # Suporte a filtragem.

```
Ou você pode clonar o projeto diretamente do GitHub:

```bash
git clone https://github.com/encode/django-rest-framework

```
Depois de instalar, adicione 'rest_framework' à configuração INSTALLED_APPS do seu projeto Django:


```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
Se você pretende usar a API navegável, é recomendável também adicionar as views de login e logout do REST Framework. Para isso, adicione o seguinte ao seu arquivo urls.py raiz:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls')),
]
```

## Considerações finais

O Django REST Framework facilita o desenvolvimento de APIs web de maneira ágil e simplificada. Conforme a documentação oficial, o DRF gera uma API navegável que melhora a usabilidade para os desenvolvedores. Além disso, o DRF oferece um sistema robusto de autenticação e serialização de dados, proporcionando um ambiente seguro e eficiente para desenvolvimento de APIs RESTful.

## Links importantes

Documentação Django Rest Framework (DRF): [https://www.django-rest-framework.org/#:~:text=Django REST framework is a,toolkit for building Web APIs.&text=The Web browsable API is,and non-ORM data sources](https://www.django-rest-framework.org/#:~:text=Django%20REST%20framework%20is%20a,toolkit%20for%20building%20Web%20APIs.&text=The%20Web%20browsable%20API%20is,and%20non%2DORM%20data%20sources).

Documentação DRF sobre serialização: https://www.django-rest-framework.org/api-guide/serializers/

Documentação DRF sobre segurança: https://www.django-rest-framework.org/api-guide/authentication/

Diferenças entre Django e DRF: https://www.alura.com.br/artigos/django-django-rest-diferencas

Curso DRF: https://www.youtube.com/watch?v=2G51oQKwXP0&list=PLnPZ9TE1Tj4BMN4I4Dce6HZ8pXiw99-gq&index=2
