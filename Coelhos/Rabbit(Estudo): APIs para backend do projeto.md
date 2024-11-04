## Estudo sobre autenticação com Django Allauth e Oauth2
## Django Allauth

O Django Allauth é uma biblioteca poderosa para gerenciar autenticação de usuários em projetos Django, com funcionalidades que facilitam tanto o login quanto o registro de novos usuários. Ela permite a autenticação via métodos tradicionais (como e-mail e senha). Isso permite que os usuários possam escolher entre criar uma conta com e-mail ou usar uma conta já existente de uma dessas plataformas.

### Principais Funcionalidades do Django Allauth

1. **Registro de Usuário**: Possui suporte completo para criação de contas com verificação de e-mail, garantindo uma segurança adicional e evitando cadastros inválidos.
2. **Autenticação com Redes Sociais**: Simplifica a integração com provedores de redes sociais (como Google e Facebook), permitindo que o usuário se autentique usando uma conta existente em uma dessas plataformas.
3. **Autenticação Multi-Fator (MFA)**: Com a configuração adequada, o Django Allauth permite adicionar camadas de segurança, como autenticação de dois fatores, oferecendo uma segurança adicional para o login dos usuários.
4. **Gerenciamento de Conta**: Oferece funcionalidades para recuperação de senha, alteração de e-mail e personalização de perfil, simplificando a gestão das informações dos usuários.
5. **Configuração Flexível**: Possibilita a customização de templates e lógica de autenticação, para que a interface e experiência do usuário estejam de acordo com a identidade visual do projeto.
6. **Compatível com Django REST Framework**: Ele pode ser usado com o Django REST Framework para autenticação em APIs, especialmente útil no caso de aplicações móveis ou SPA (Single Page Application).

# Oauth2

O OAuth 2.0 é um protocolo padrão para autorização. Permite que aplicativos como Web App, Mobile e Desktop obtenham acesso limitado às informações de usuários através do protocolo HTTP.Estrutura de autorição para aplicações que utilizam HTTP. É um proyocolo padrão para autorização.

Roles (Papéis)

O OAuth 2.0 define quatro roles.

1. Resource Owner - É a pessoa (entidade) que concede o acesso aos seus dados. Literalmente o **Dono do Recurso**. É como o OAuth 2.0 classifica o usuário.
2. Resource Server - É a API.
Exposta na internet e contém os dados do Usuário. Para conseguir acesso
ao seu conteúdo é necessário um token emitido pelo Authorization Server.
3. Authorization Server - Responsável por autenticação e emitir tokens de acesso (Access Token). Detém informações dos Resource Owner (Usuários) e expõe no formato de Claims através do **Bearer Token**. Autentica e interage com o usuário após identificar e autorizar o client.
4. Client - É a aplicação que interage com o Resource Owner. No caso de uma App Web, seria a aplicação do Browser.

### Como esses papéis se interagem com Google Accounts:

Quando um usuário opta por autenticar-se em um aplicativo usando sua conta Google:

1. O *Client* (Achei-UnB) redireciona o usuário ao *Authorization Server* do Google, solicitando acesso a certos recursos.
2. O *Authorization Server* do Google autentica o usuário e solicita que ele conceda permissão para o *Client* acessar os dados solicitados.
3. Após o consentimento, o *Authorization Server* emite um *Access Token*, que é então usado pela aplicação como um *Bearer Token* para acessar o *Resource Server* (neste caso, a API do Google).
4. O *Client* pode então acessar os dados permitidos no *Resource Server*, usando o token emitido para autenticar as requisições.

# Fluxo de autenticação

Este é fluxo padrão do protocolo. Demonstra de forma simplificada o relacionamento e os papéis dos envolvidos.

![oauth2](https://github.com/user-attachments/assets/09c54a2e-6622-4475-9aa5-88f4332c14d0)

Explicando o fluxo de uma maneira prática.

- (A) O Usuário acessa um client. Para ter acesso ao conteúdo protegido da api (**Resource Server**) o client (A) Solicita Autorização(implicity) ao Resource Owner.
- (B) A **Autorização é Concedida** pelo usuário (**Resource Owner**) ao, por exemplo, clicar no botão Continuar com o Google.
- (C) O client solicita um token de acesso ao Authorization Server através da autenticação de sua própria identidade.
- (D) O Usuário (**Resource Owner**) confirma sua identidade através do seu usuário e senha ou através de um terceiro (Facebook, Google). Se tudo ocorrer bem um Access Token será criado e devolvido para o client gerenciar.
- (E) Por fim o client informa o Access Token ao Resorce Server.
- (F) O Resource Server faz validação e retorna o **Conteúdo Protegido**.

O fluxo pode diferenciar, dependendo da configuração da aplicação, 
como por exemplo no Password flow, onde o cliente não é redirecionado 
para o Authorization Server.

[Documentação Allauth](https://django-allauth.readthedocs.io/en/latest/)

[Artigo sobre Oauth2](https://www.brunobrito.net.br/oauth2/)

---

## Estudo sobre Django Forms

### Formulários em HTML

Em HTML, um formulário é uma coleção de elementos dentro de `<form>...</form>` que permitem ao visitante fazer coisas como:

- Inserir texto,
- Selecionar opções,
- Manipular objetos ou controles,

Em seguida, o usuário pode enviar essas informações de volta ao servidor.

Alguns desses elementos de interface de formulário, como entradas de texto ou caixas de seleção, são incorporados ao próprio HTML. Outros elementos são mais complexos; por exemplo, uma interface que exibe um seletor de data ou permite mover um controle deslizante. Para esses, geralmente são usados **JavaScript** e **CSS**, além dos elementos `<input>` do HTML.

Além dos elementos `<input>`, um formulário precisa especificar:

- **onde**: a URL para onde os dados correspondentes à entrada do usuário devem ser enviados;
- **como**: o método HTTP (GET ou POST) pelo qual os dados devem ser enviados.

---

### GET e POST

**GET** e **POST** são os únicos métodos HTTP usados para lidar com formulários.

- **POST**: O formulário de login do Django, por exemplo, é enviado usando o método POST. Nesse caso, o navegador:
  1. Agrupa os dados do formulário,
  2. Codifica para transmissão,
  3. Envia para o servidor,
  4. Recebe uma resposta.

- **GET**: O GET, por outro lado, agrupa os dados em uma string e usa isso para compor uma URL, incluindo as chaves e valores dos dados. 

**Usos recomendados**:
- Qualquer solicitação que possa **alterar o estado do sistema** - como mudanças no banco de dados - deve usar POST.
- **GET** deve ser usado apenas para solicitações que **não afetam o estado do sistema**.

**Segurança**:
- **GET** não é adequado para um formulário de senha, pois a senha apareceria na URL, visível no histórico do navegador e logs do servidor.
- **POST** é mais seguro, especialmente quando combinado com proteções, como a **proteção CSRF** do Django, que oferece controle de acesso adicional.

Por outro lado, GET é adequado para funcionalidades como formulários de busca na web, pois as URLs podem ser facilmente **marcadas como favorito, compartilhadas ou reenviadas**.

---

### A Classe Form do Django

No centro desse sistema está a classe `Form` do Django. Semelhante aos modelos do Django, a classe `Form`:

- Descreve a estrutura de um formulário,
- Determina o comportamento e a aparência do formulário.

#### Campos de um Formulário

- **Mapeamento**: Campos de uma classe de formulário mapeiam para elementos `<input>` de um formulário HTML.
- **ModelForm**: Um `ModelForm` mapeia os campos de uma classe de modelo para elementos `<input>`, como no caso do admin do Django.
- **Classes de campo**: Cada campo de um formulário é uma classe que gerencia dados e realiza validação.
  - Exemplo: `DateField` e `FileField` lidam com tipos de dados muito diferentes e executam funções distintas.

Cada campo de formulário é representado ao usuário como um **widget HTML** (elemento de interface). Cada tipo de campo tem uma **classe de widget padrão**, mas esses widgets podem ser sobrescritos conforme necessário.

---

### Instanciação, Processamento e Renderização de Formulários

Ao renderizar um objeto no Django, normalmente:

1. Obtemos o objeto na **view** (buscando-o no banco de dados, por exemplo);
2. Passamos o objeto para o **contexto do template**;
3. Expandimos o objeto para HTML usando **variáveis de template**.

Para um formulário:

- **Renderizar um formulário vazio** faz sentido, pois queremos que o usuário o preencha.
- Quando manipulamos um formulário em uma view, normalmente o **instanciamos** ali, podendo deixá-lo vazio ou preenchido previamente.

Ao instanciar um formulário, podemos optar por deixá-lo vazio ou preenchê-lo previamente, por exemplo com:

  1. dados de uma instância de modelo salva (como no caso de formulários de administração para edição)
  2. dados que coletamos de outras fontes
  3. dados recebidos de um envio anterior de formulário HTML

 ### Construindo um formulário no Django
### forms.py

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Seu nome", max_length=100)
```
Neste exemplo, criamos um formulário básico usando a classe Form do Django. O campo your_name é do tipo CharField, que cria um campo de texto no formulário com o rótulo "Seu nome" e permite um comprimento máximo de 100 caracteres.

Porém é necessário que se esboçe o código HTML para que o form leia corretamente a URL.

[Documentação Django Forms](https://docs.djangoproject.com/en/5.1/topics/forms/#html-forms)

[Cuso Django Forms](https://www.youtube.com/playlist?list=PLaUQIPIyD0z43DiRKM0x8YNEB-1QNCOwR)

---

## Estudo sobre Django Message

### O framework de mensagens

Comumente, em aplicações web, é necessário exibir uma mensagem de notificação de uma única vez (também conhecida como "flash message") ao usuário após o processamento de um formulário ou de outros tipos de entrada do usuário.

Para isso, o Django oferece suporte total para mensagens baseadas em cookies e sessões, tanto para usuários anônimos quanto para usuários autenticados. O framework de mensagens permite que você armazene temporariamente mensagens em uma solicitação e as recupere para exibição em uma solicitação subsequente (geralmente a próxima). Cada mensagem é marcada com um nível específico que determina sua prioridade (por exemplo, info, warning ou error).

### Habilitando mensagens

As mensagens são implementadas por meio de uma classe de middleware e do respectivo processador de contexto.

As configurações padrão do `settings.py` criadas pelo `django-admin startproject` já contêm todas as configurações necessárias para habilitar a funcionalidade de mensagens:

- `'django.contrib.messages'` está em `INSTALLED_APPS`.
- `MIDDLEWARE` contém `'django.contrib.sessions.middleware.SessionMiddleware'` e `'django.contrib.messages.middleware.MessageMiddleware'`.
- O backend de armazenamento padrão depende de sessões. Por isso, o `SessionMiddleware` deve ser habilitado e aparecer antes do `MessageMiddleware` em `MIDDLEWARE`.
- A opção `'context_processors'` do backend `DjangoTemplates`, definida em sua configuração `TEMPLATES`, contém `'django.contrib.messages.context_processors.messages'`.

### Configurando o mecanismo de mensagens

### Backends de armazenamento

O framework de mensagens pode usar diferentes backends para armazenar mensagens temporárias.

O Django fornece três classes de armazenamento integradas em `django.contrib.messages`:

**class storage.session.SessionStorage**

Essa classe armazena todas as mensagens dentro da sessão da requisição. Portanto, requer o aplicativo `contrib.sessions` do Django.

**class storage.cookie.CookieStorage**

Essa classe armazena os dados da mensagem em um cookie (assinados com um hash secreto para evitar manipulação) para persistir notificações entre requisições. Mensagens antigas são descartadas se o tamanho dos dados do cookie exceder 2048 bytes.

**class storage.fallback.FallbackStorage**

Essa classe primeiro utiliza o `CookieStorage` e recorre ao `SessionStorage` para as mensagens que não puderam caber em um único cookie. Também requer o aplicativo `contrib.sessions` do Django.

Esse comportamento evita a gravação na sessão sempre que possível, proporcionando o melhor desempenho no caso geral.

O `FallbackStorage` é a classe de armazenamento padrão. Se não for adequada às suas necessidades, você pode selecionar outra classe de armazenamento definindo `MESSAGE_STORAGE` para seu caminho completo de importação, por exemplo:

```python
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
```

**class storage.base.BaseStorage**

Para escrever sua própria classe de armazenamento, herde a classe `BaseStorage` em `django.contrib.messages.storage.base` e implemente os métodos `_get` e `_store`.

### Níveis de mensagens

O framework de mensagens é baseado em uma arquitetura de níveis configurável, semelhante à do módulo de logging do Python. Os níveis de mensagem permitem agrupar mensagens por tipo, para que possam ser filtradas ou exibidas de maneira diferente nas views e templates.

Os níveis integrados, que podem ser importados diretamente de `django.contrib.messages`, são:

| Constante | Propósito |
| --- | --- |
| DEBUG | Mensagens relacionadas ao desenvolvimento que serão ignoradas (ou removidas) em uma implantação de produção |
| INFO | Mensagens informativas para o usuário |
| SUCCESS | Uma ação foi bem-sucedida, por exemplo, "Seu perfil foi atualizado com sucesso" |
| WARNING | Uma falha não ocorreu, mas pode ser iminente |
| ERROR | Uma ação não foi bem-sucedida ou alguma outra falha ocorreu |

A configuração `MESSAGE_LEVEL` pode ser usada para mudar o nível mínimo registrado (ou pode ser alterado por requisição). Tentativas de adicionar mensagens de um nível inferior a este serão ignoradas.

### Tags de mensagens

As tags de mensagens são uma representação em string do nível da mensagem, além de quaisquer tags extras que foram adicionadas diretamente na view (veja "Adicionando tags de mensagem extras" abaixo para mais detalhes). As tags são armazenadas em uma string e são separadas por espaços. Normalmente, as tags de mensagens são usadas como classes CSS para personalizar o estilo da mensagem com base no tipo de mensagem. Por padrão, cada nível tem uma única tag que é uma versão minúscula de sua própria constante:

| Nível Constante | Tag |
| --- | --- |
| DEBUG | debug |
| INFO | info |
| SUCCESS | success |
| WARNING | warning |
| ERROR | error |

Para alterar as tags padrão para um nível de mensagem (seja integrado ou personalizado), defina a configuração `MESSAGE_TAGS` como um dicionário contendo os níveis que você deseja alterar. Como isso estende as tags padrão, você só precisa fornecer tags para os níveis que deseja sobrescrever.

[Documentação Django Message](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/)

---

## Pillow

Pillow é uma biblioteca Python que oferece uma série de funcionalidades para abrir, manipular e salvar diferentes formatos de imagem

Pillow permite realizar operações como:

- Redimensionamento e recorte de imagens
- Aplicação de filtros e efeitos
- Conversão entre diferentes formatos de imagem
- Adição de texto e gráficos a imagens
- Processamento em lote de imagens

### Benefícios do uso do Pillow com Django

- **Flexibilidade**: Permite uma ampla gama de manipulações de imagem, desde as mais simples até as mais complexas.
- **Integração**: Funciona bem com o sistema de upload de arquivos do Django, facilitando o gerenciamento de imagens.
- **Suporte a Vários Formatos**: Pillow suporta uma variedade de formatos de imagem, como JPEG, PNG, GIF, entre outros.

### Como usar Pillow no Django

Para usar Pillow em um projeto Django, você deve seguir alguns passos:

1. **Instalação**:
Você pode instalar Pillow usando pip:
    
    ```bash
    pip install Pillow
    ```
    
2. **Configuração do modelo**:
Ao trabalhar com imagens em Django, você geralmente as armazena em um campo de modelo. Para isso, você deve usar o campo `ImageField`. Por exemplo:

```python
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
```

3. **Manipulação de Imagens**:
Uma vez que você tenha a imagem carregada, pode usar as funcionalidades do Pillow para manipulá-la. Por exemplo, para redimensionar uma imagem:

```python
from PIL import Image
from django.core.files.base import ContentFile

def process_image(image_file):
    image = Image.open(image_file)
    image = image.resize((800, 800))  # Redimensiona a imagem para 800x800
    image_io = BytesIO()
    image.save(image_io, format='JPEG')
    return ContentFile(image_io.getvalue(), name=image_file.name)
```

4. **Exibição de Imagens**:
No Django, você pode exibir imagens em seus templates usando a URL do campo `ImageField`:

```html
<img src="{{ my_model.image.url }}" alt="My Image">
```


![image](https://github.com/user-attachments/assets/735dd0ba-09a3-47d3-bbd0-030b137ce145)

Exemplo onde a Pillow redimenciona a imagem.

[Documentação PIllow](https://pillow.readthedocs.io/en/stable/index.html)

---

# Estudo sobre tecnologias Back-end

Frameworks: Django(Signals, Filter, REST, Channels, private-chat2, Allauth, Messages, Forms)

Bibliotecas: Pillow, Celery

Banco de dados: PostgreSQL, DBeaver

OAuth2 e SAML

# Django - Estrutura, Banco de Dados e Notificações

### O que é Django?

Django é um framework web de código aberto em Python que facilita a criação de aplicações web escaláveis e seguras, promovendo um desenvolvimento rápido e um design limpo. É popular por sua sintaxe simples e robustez, sendo utilizado em diversas áreas, como machine learning e análise de dados.

### Para que serve?

Django é usado para:

- **Criação de sites e aplicações web**: Desde sites simples até sistemas complexos.
- **Plataformas de redes sociais**: Exemplo: Instagram e Pinterest.
- **Sistemas de gerenciamento interno**: Ferramentas para empresas, como gerenciamento de projetos.
- **Aplicações e-commerce**: Gerenciamento de produtos e pagamentos.
- **APIs**: Backend para aplicativos móveis e criação de APIs.

### Como funciona?

Django utiliza a arquitetura MVT (Model-View-Template), uma variação do padrão MVC. Os principais componentes incluem:

- **Modelos**: Estruturas de dados que representam tabelas no banco de dados.
- **Views**: Lógica que processa requisições e retorna respostas.
- **Templates**: Arquivos HTML dinâmicos que geram a interface do usuário.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/b11a9623-59a8-48d4-b8e6-13a3e64f0079/image.png)

### Estrutura de um Projeto Django

Um projeto Django contém arquivos principais como `manage.py`, `settings.py`, e `urls.py`, além de diretórios para aplicativos que incluem `views.py`, `models.py` e `templates/`.

### Resumo

Django é uma ferramenta poderosa para desenvolvimento web, oferecendo uma abordagem estruturada e eficiente para criar aplicações robustas, tornando o processo mais ágil e organizado.

---

## Configuração do PostgreSQL para Django

1. **Acesso ao PostgreSQL**: Iniciar sessão com o usuário `postgres`:
    
    ```bash
    sudo -u postgres psql
    ```
    
2. **Criação do Banco de Dados**: Criar um banco de dados para o projeto.
3. **Criação de Usuário**: Criar um usuário com senha:
    
    ```sql
    CREATE USER myprojectuser WITH PASSWORD 'password';
    ```
    
4. **Definição de Parâmetros**:
    
    ```sql
    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ```
    
5. **Concessão de Permissões**:
    
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    ```
    
6. **Configuração no Django**: Adicionar as configurações de banco de dados no `settings.py`:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'myproject',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
    

## Consultas Otimizadas no ORM do Django para o AcheiUnB

1. **`select_related`** para Foreign Keys.
2. **`prefetch_related`** para ManyToMany.
3. **Limitar Campos** com `only` e `defer`.
4. **Filtrar Resultados** para reduzir a carga.
5. **Usar `count()`** em vez de `len()`.
6. **Anotações com `annotate`** para agregações.
7. **Indexação** de campos frequentemente filtrados.
8. **Evitar N+1** com `select_related` e `prefetch_related`.
9. **Consultas Personalizadas** com SQL raw.
10. **Utilização de `F` e `Q`** para condições complexas.

## Ferramentas de Gerenciamento de Banco de Dados com DBeaver

- **Instalação**: Baixar no site oficial.
- **Configuração da Conexão**: Conectar ao PostgreSQL com credenciais.
- **Execução de Queries**: Editor SQL para gerenciamento visual.
- **Análise de Performance**: Uso do “Explain Plan” para otimizações.
- **Exportação/Importação**: Facilita backups e integrações.
- **Gerenciamento de Usuários**: Controle de permissões no banco.

### Recursos Adicionais do DBeaver

- **Interface Personalizável** e suporte a múltiplos SGBDs.
- **Histórico de Queries** para reutilização.

---

### Materiais de Referência

Para mais detalhes sobre cada tópico, consulte:

- Pasta dos [Coelhos](https://github.com/unb-mds/2024-2-AcheiUnB/blob/main/Coelhos/Rabbit(Estudo)%3A%20PostgreSQL%20para%20Django.md).
- Adaptações e contribuições por [Euller Júlio](https://github.com/Potatoyz908).

---

### Introdução ao Django Channels, Celery e Redis para Tarefas Assíncronas e Comunicação em Tempo Real

---

### **1. Configuração do Django Channels**

- **Introdução ao Channels para Comunicação em Tempo Real**
    - O Django Channels permite adicionar funcionalidades de comunicação em tempo real a aplicações Django, possibilitando eventos como chat ao vivo, atualizações instantâneas e notificações.
    - **(Espaço para imagem do fluxo de comunicação com Channels)**
- **Configuração e Uso Básico**
    - Passos iniciais para instalação e configuração do Django Channels, incluindo definição de WebSockets e integração com o Django.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/43c7a60d-c956-43c0-8b74-b884316991d1/image.png)

---

### **2. Configuração do Celery**

- **Instalação e Configuração do Celery para Tarefas Assíncronas**
    - O Celery é uma ferramenta poderosa para gerenciamento de tarefas assíncronas. Ele facilita o processamento de tarefas em segundo plano, ideal para operações demoradas, como processamento de dados e envio de emails.
    - **(Espaço para imagem da arquitetura de filas com Celery)**
- **Integração do Celery com Django**
    - Passo a passo para integrar o Celery com o Django, incluindo criação de tarefas e teste de execução.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/0ae82c62-c3c5-477b-bcc7-4e4e504559db/image.png)

---

### **3. Integração do Redis com Django e Celery**

- **Instalação do Redis e Configuração como Broker para o Celery**
    - Redis é um banco de dados em memória que serve como “broker” para o Celery, gerenciando as filas de mensagens entre tarefas assíncronas.
    - **(Espaço para imagem do Redis configurado como broker do Celery)**
- **Testes e Exemplos de Notificações Assíncronas**
    - Demonstrações de uso prático do Redis e Celery para enviar notificações e mensagens em tempo real, complementando a configuração com Django Channels.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/6532e8e5-8cab-4555-87a2-2954be02e854/image.png)
    

---

### **Materiais de Referência**

- [Django Channels Documentation](https://channels.readthedocs.io/en/stable/) - Documentação oficial do Django Channels, com guias de configuração e exemplos práticos.
- [Celery Documentation](https://docs.celeryproject.org/) - Guia detalhado do Celery, incluindo integração com Django e configurações avançadas.
- [Configuração de Redis para Django e Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/) - Tutorial sobre uso do Redis como broker para tarefas assíncronas com Celery e Django Channels.

---

# Configuração e Uso de Signals no Django

## Introdução ao Conceito de Signals no Django

Signals são ferramentas úteis no Django para permitir que certos componentes da aplicação se comuniquem entre si, especialmente quando queremos que uma ação em um modelo desencadeie automaticamente outra ação em outra parte do sistema.

Por exemplo, podemos utilizar signals para enviar notificações ou atualizar dados sempre que determinado evento ocorrer, como a criação ou atualização de um objeto.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/aef04d2b-4100-4056-89fa-7cee4c55951d/image.png)

## Criação de Signals Personalizados e Conexão com Modelos

No Django, podemos criar signals personalizados que se conectam a eventos específicos dos modelos. Os signals são definidos em arquivos específicos e devem ser "conectados" a funções que realizarão as ações necessárias. Algumas das ações comuns são o envio de mensagens de confirmação de cadastro, notificações para alterações em campos específicos, entre outros.

### Passos para Configuração de um Signal:

1. Criar um arquivo de signals na aplicação desejada.
2. Definir o signal com as ações específicas que ele deve executar.
3. Conectar o signal ao evento específico do modelo (como `post_save`, `pre_delete`).
4. Configurar o arquivo `apps.py` para registrar os signals.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/46d8ad3d-3565-440c-b1c6-fd431b7a97a3/image.png)

# Exemplo de Automação com Notificações

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/14dd28eb-a650-4a47-80b5-7f8ed412c08c/image.png)

## Automatização de Envio de Notificações ou Atualizações com Signals

Os signals são amplamente utilizados para automatizar o envio de notificações ou atualizações de dados no sistema. Por exemplo, ao criar um novo usuário, podemos configurar um signal para enviar automaticamente uma mensagem de boas-vindas ou gerar um log de atividade.

### Exemplo Prático:

No projeto, um signal pode ser configurado para enviar uma notificação por e-mail sempre que um novo post é criado ou quando um comentário é adicionado a um artigo. Essa abordagem permite manter a comunicação entre partes do sistema sem a necessidade de chamadas explícitas e manuais.

Este exemplo ajuda a compreender como os signals facilitam a automação de tarefas e mantém o código organizado, evitando repetição de lógica em múltiplas partes do sistema.

---

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

![DRF_Serialização.webp](https://prod-files-secure.s3.us-west-2.amazonaws.com/16d14aaf-a003-4497-b37b-e02ade722756/9c001abb-9508-4d70-810e-0efc94a3b12f/DRF_Serializao.webp)

## Segurança no DRF (Django Rest Framework)

### 1. **Autenticação**

- **OAuth2**: DRF também pode ser integrado ao OAuth2 para permitir autenticação segura e autorização em plataformas de terceiros, como Google ou Facebook.

### 2. **Autorização**

- **Permissions**: DRF permite configurar permissões de acesso para cada endpoint, definindo regras sobre quem pode acessar ou modificar os dados.
    - **AllowAny**: Permite acesso a qualquer usuário.
- **Permissões personalizadas**: DRF permite criar regras específicas, como permitir o acesso apenas ao proprietário de um recurso.

### 3. **Throttle (Limite de Requisições)**

- **Throttle** (ou rate limiting) controla o número de requisições que um usuário pode fazer em um determinado período de tempo.
- Isso ajuda a evitar ataques de força bruta, como tentativas de login em massa ou sobrecarga do sistema.
- DRF oferece throttles de escopo por usuário, anônimo ou global, que podem ser personalizados.

### 4. **Validação de Dados**

- O DRF fornece ferramentas robustas de validação para impedir que dados mal formatados ou não confiáveis sejam processados.
- A validação é feita automaticamente com base nos serializers, e regras personalizadas podem ser adicionadas conforme necessário.

### 5. **Proteção Contra CSRF (Cross-Site Request Forgery)**

- DRF usa tokens CSRF para proteger as sessões de usuários contra ataques CSRF.
- CSRF é mais relevante para aplicações web que usam cookies de sessão, mas também pode ser relevante em certos contextos de API.

### 6. **Proteção Contra Cross-Site Scripting (XSS) e Injeção de SQL**

- DRF herda as proteções contra XSS e injeção de SQL do Django. As consultas ao banco de dados são parametrizadas, o que evita que dados inseridos pelo usuário modifiquem a estrutura das consultas SQL.
- Para XSS, o Django realiza uma sanitização automática de dados exibidos em templates HTML, protegendo a aplicação contra scripts maliciosos.

### 7. **Criptografia e HTTPS**

- Embora não seja exclusivo do DRF, é fundamental que APIs sejam acessadas apenas por **HTTPS** para garantir a criptografia dos dados transmitidos.
- O DRF facilita o uso de headers e configurações de segurança, mas a criptografia é uma configuração a ser feita no nível do servidor.

### 8. **Proteção Contra Exposição de Informações Sensíveis**

- É importante garantir que dados sensíveis, como senhas, tokens de API e detalhes de autenticação, sejam adequadamente protegidos.
- DRF permite definir quais campos serão exibidos em respostas usando serializers e fornece métodos para garantir que dados sensíveis não sejam expostos.

### 9. **Logs e Monitoramento de Segurança**

- DRF permite que você monitore e registre atividades, o que é útil para identificar e responder a acessos ou tentativas de acessos suspeitos.

## Principais utilizações do DRF no nosso projeto

Usaremos as ferramentas do DRF para criar APIs para a busca dentro do nosso site e para  iteração dos usuários, fazendo uso da parte de autentificação do DRF, com o OAuth2. Utilizaremos também a autorização, os limites de requisições, ****proteção Contra Cross-Site Scripting (XSS) e Injeção de SQL, https,

## Considerações finais

O Django REST Framework facilita o desenvolvimento de APIs web de maneira ágil e simplificada. Conforme a documentação oficial, o DRF gera uma API navegável que melhora a usabilidade para os desenvolvedores. Além disso, o DRF oferece um sistema robusto de autenticação e serialização de dados, proporcionando um ambiente seguro e eficiente para desenvolvimento de APIs RESTful.

## Links importantes

- [Django Channels Documentation](https://channels.readthedocs.io/en/stable/) - Documentação oficial do Django Channels, com guias de configuração e exemplos práticos.
- [Celery Documentation](https://docs.celeryproject.org/) - Guia detalhado do Celery, incluindo integração com Django e configurações avançadas.
- [Configuração de Redis para Django e Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/) - Tutorial sobre uso do Redis como broker para tarefas assíncronas com Celery e Django Channels.
- [Documentação do Django sobre Signals](https://docs.djangoproject.com/en/4.0/topics/signals/)
- Documentação Django Rest Framework (DRF): [https://www.django-rest-framework.org/#:~:text=Django REST framework is a,toolkit for building Web APIs.&text=The Web browsable API is,and non-ORM data sources](https://www.django-rest-framework.org/#:~:text=Django%20REST%20framework%20is%20a,toolkit%20for%20building%20Web%20APIs.&text=The%20Web%20browsable%20API%20is,and%20non%2DORM%20data%20sources).
- Documentação DRF sobre serialização: https://www.django-rest-framework.org/api-guide/serializers/
- Documentação DRF sobre segurança: https://www.django-rest-framework.org/api-guide/authentication/
- Diferenças entre Django e DRF: https://www.alura.com.br/artigos/django-django-rest-diferencas

---

## Estudo sobre autenticação com Django Allauth e Oauth2

## Django Allauth

O Django Allauth é uma biblioteca poderosa para gerenciar autenticação de usuários em projetos Django, com funcionalidades que facilitam tanto o login quanto o registro de novos usuários. Ela permite a autenticação via métodos tradicionais (como e-mail e senha). Isso permite que os usuários possam escolher entre criar uma conta com e-mail ou usar uma conta já existente de uma dessas plataformas.

### Principais Funcionalidades do Django Allauth

1. **Registro de Usuário**: Possui suporte completo para criação de contas com verificação de e-mail, garantindo uma segurança adicional e evitando cadastros inválidos.
2. **Autenticação com Redes Sociais**: Simplifica a integração com provedores de redes sociais (como Google e Facebook), permitindo que o usuário se autentique usando uma conta existente em uma dessas plataformas.
3. **Autenticação Multi-Fator (MFA)**: Com a configuração adequada, o Django Allauth permite adicionar camadas de segurança, como autenticação de dois fatores, oferecendo uma segurança adicional para o login dos usuários.
4. **Gerenciamento de Conta**: Oferece funcionalidades para recuperação de senha, alteração de e-mail e personalização de perfil, simplificando a gestão das informações dos usuários.
5. **Configuração Flexível**: Possibilita a customização de templates e lógica de autenticação, para que a interface e experiência do usuário estejam de acordo com a identidade visual do projeto.
6. **Compatível com Django REST Framework**: Ele pode ser usado com o Django REST Framework para autenticação em APIs, especialmente útil no caso de aplicações móveis ou SPA (Single Page Application).

Em nossa aplicação é possível a utilização de apenas o sistema de permições e escopos do DRF e Oauth2, como no SuaGrade-UnB. Porém se quisermos fazer um sistema para que os usuários se cadastrem dentro do nosso aplicativo possam assim modificar usuário e etc precisaremos utilizar o Allauth, que ainda permite a imtegralização com o Google Accounts via Oauth2.

# Oauth2

O OAuth 2.0 é um protocolo padrão para autorização. Permite que aplicativos como Web App, Mobile e Desktop obtenham acesso limitado às informações de usuários através do protocolo HTTP.Estrutura de autorição para aplicações que utilizam HTTP. É um proyocolo padrão para autorização.

Roles (Papéis)

O OAuth 2.0 define quatro roles.

1. Resource Owner - É a pessoa (entidade) que concede o acesso aos seus dados. Literalmente o **Dono do Recurso**. É como o OAuth 2.0 classifica o usuário.
2. Resource Server - É a API.
Exposta na internet e contém os dados do Usuário. Para conseguir acesso
ao seu conteúdo é necessário um token emitido pelo Authorization Server.
3. Authorization Server - Responsável por autenticação e emitir tokens de acesso (Access Token). Detém informações dos Resource Owner (Usuários) e expõe no formato de Claims através do **Bearer Token**. Autentica e interage com o usuário após identificar e autorizar o client.
4. Client - É a aplicação que interage com o Resource Owner. No caso de uma App Web, seria a aplicação do Browser.

### Como esses papéis se interagem com Google Accounts:

Quando um usuário opta por autenticar-se em um aplicativo usando sua conta Google:

1. O *Client* (Achei-UnB) redireciona o usuário ao *Authorization Server* do Google, solicitando acesso a certos recursos.
2. O *Authorization Server* do Google autentica o usuário e solicita que ele conceda permissão para o *Client* acessar os dados solicitados.
3. Após o consentimento, o *Authorization Server* emite um *Access Token*, que é então usado pela aplicação como um *Bearer Token* para acessar o *Resource Server* (neste caso, a API do Google).
4. O *Client* pode então acessar os dados permitidos no *Resource Server*, usando o token emitido para autenticar as requisições.

# Fluxo de autenticação

Este é fluxo padrão do protocolo. Demonstra de forma simplificada o relacionamento e os papéis dos envolvidos.

!https://www.brunobrito.net.br/content/images/2018/08/roles-2.png

Explicando o fluxo de uma maneira prática.

- (A) O Usuário acessa um client. Para ter acesso ao conteúdo protegido da api (**Resource Server**) o client (A) Solicita Autorização(implicity) ao Resource Owner.
- (B) A **Autorização é Concedida** pelo usuário (**Resource Owner**) ao, por exemplo, clicar no botão Continuar com o Google.
- (C) O client solicita um token de acesso ao Authorization Server através da autenticação de sua própria identidade.
- (D) O Usuário (**Resource Owner**) confirma sua identidade através do seu usuário e senha ou através de um terceiro (Facebook, Google). Se tudo ocorrer bem um Access Token será criado e devolvido para o client gerenciar.
- (E) Por fim o client informa o Access Token ao Resorce Server.
- (F) O Resource Server faz validação e retorna o **Conteúdo Protegido**.

O fluxo pode diferenciar, dependendo da configuração da aplicação, 
como por exemplo no Password flow, onde o cliente não é redirecionado 
para o Authorization Server.

[Documentação Allauth](https://django-allauth.readthedocs.io/en/latest/)

[Artigo sobre Oauth2](https://www.brunobrito.net.br/oauth2/)

---

## Estudo sobre Django Forms e Message

O **Django Forms** é um módulo do Django que simplifica a criação, exibição e validação de formulários HTML em aplicações web. Ele permite capturar dados de usuários com segurança e praticidade, validando automaticamente as entradas e exibindo erros amigáveis. Com Django Forms, é possível definir formulários personalizados usando classes Python e criar campos como texto, e-mail, datas e mais. Além disso, o módulo facilita a conexão de formulários com modelos de banco de dados, automatizando o processo de entrada de dados e tornando o desenvolvimento de formulários mais rápido e seguro.

### Formulários em HTML

Em HTML, um formulário é uma coleção de elementos dentro de `<form>...</form>` que permitem que o visitante faça coisas como inserir texto, selecionar opções, manipular objetos ou controles e, em seguida, envie essas informações de volta ao servidor.

Alguns desses elementos de interface de formulário - como entrada de texto ou caixas de seleção - são incorporados ao próprio HTML. Outros são bem mais complexos; uma interface que exibe um seletor de data ou permite mover um controle deslizante ou manipular controles geralmente usa JavaScript e CSS, além dos elementos `<input>` do HTML para atingir esses efeitos.

Além dos elementos `<input>`, um formulário deve especificar duas coisas:

1. **onde**: a URL para onde os dados correspondentes à entrada do usuário devem ser enviados
2. **como**: o método HTTP pelo qual os dados devem ser enviados

### GET e POST

GET e POST são os únicos métodos HTTP usados para lidar com formulários.

O formulário de login do Django é enviado usando o método POST, em que o navegador agrupa os dados do formulário, os codifica para transmissão, envia para o servidor e então recebe a resposta.

### Construindo um formulário no Django

### A classe Form

Já sabemos como queremos que nosso formulário HTML pareça. Nosso ponto de partida para isso no Django é o seguinte:

### forms.py

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Seu nome", max_length=100)
```

### Django Messages

O `django.contrib.messages` é uma framework de mensagens para exibir notificações temporárias aos usuários. Essas mensagens podem informar sobre o sucesso ou falha de uma ação, como uma mensagem de "Cadastro realizado com sucesso" ou "Erro ao enviar o formulário".

### O framework de mensagens

Comumente, em aplicações web, é necessário exibir uma mensagem de notificação de uma única vez (também conhecida como "flash message") ao usuário após o processamento de um formulário ou de outros tipos de entrada do usuário.

Para isso, o Django oferece suporte total para mensagens baseadas em cookies e sessões, tanto para usuários anônimos quanto para usuários autenticados. O framework de mensagens permite que você armazene temporariamente mensagens em uma solicitação e as recupere para exibição em uma solicitação subsequente (geralmente a próxima). Cada mensagem é marcada com um nível específico que determina sua prioridade (por exemplo, info, warning ou error).

### Configurando o mecanismo de mensagens

### Backends de armazenamento

O framework de mensagens pode usar diferentes backends para armazenar mensagens temporárias.

O Django fornece três classes de armazenamento integradas em `django.contrib.messages`:

### Níveis de mensagens

O framework de mensagens é baseado em uma arquitetura de níveis configurável, semelhante à do módulo de logging do Python. Os níveis de mensagem permitem agrupar mensagens por tipo, para que possam ser filtradas ou exibidas de maneira diferente nas views e templates.

Os níveis integrados, que podem ser importados diretamente de `django.contrib.messages`, são:

| Constante | Propósito |
| --- | --- |
| DEBUG | Mensagens relacionadas ao desenvolvimento que serão ignoradas (ou removidas) em uma implantação de produção |
| INFO | Mensagens informativas para o usuário |
| SUCCESS | Uma ação foi bem-sucedida, por exemplo, "Seu perfil foi atualizado com sucesso" |
| WARNING | Uma falha não ocorreu, mas pode ser iminente |
| ERROR | Uma ação não foi bem-sucedida ou alguma outra falha ocorreu |

A configuração `MESSAGE_LEVEL` pode ser usada para mudar o nível mínimo registrado (ou pode ser alterado por requisição). Tentativas de adicionar mensagens de um nível inferior a este serão ignoradas.

### Tags de mensagens

As tags de mensagens são uma representação em string do nível da mensagem, além de quaisquer tags extras que foram adicionadas diretamente na view (veja "Adicionando tags de mensagem extras" abaixo para mais detalhes). As tags são armazenadas em uma string e são separadas por espaços. Normalmente, as tags de mensagens são usadas como classes CSS para personalizar o estilo da mensagem com base no tipo de mensagem. Por padrão, cada nível tem uma única tag que é uma versão minúscula de sua própria constante:

| Nível Constante | Tag |
| --- | --- |
| DEBUG | debug |
| INFO | info |
| SUCCESS | success |
| WARNING | warning |
| ERROR | error |

Para alterar as tags padrão para um nível de mensagem (seja integrado ou personalizado), defina a configuração `MESSAGE_TAGS` como um dicionário contendo os níveis que você deseja alterar. Como isso estende as tags padrão, você só precisa fornecer tags para os níveis que deseja sobrescrever.

## Pillow

Pillow é uma biblioteca Python que oferece uma série de funcionalidades para abrir, manipular e salvar diferentes formatos de imagem

Pillow permite realizar operações como:

- Redimensionamento e recorte de imagens
- Aplicação de filtros e efeitos
- Conversão entre diferentes formatos de imagem
- Adição de texto e gráficos a imagens
- Processamento em lote de imagens

### Benefícios do uso do Pillow com Django

- **Flexibilidade**: Permite uma ampla gama de manipulações de imagem, desde as mais simples até as mais complexas.
- **Integração**: Funciona bem com o sistema de upload de arquivos do Django, facilitando o gerenciamento de imagens.
- **Suporte a Vários Formatos**: Pillow suporta uma variedade de formatos de imagem, como JPEG, PNG, GIF, entre outros.

### Como usar Pillow no Django

Para usar Pillow em um projeto Django, você deve seguir alguns passos:

1. **Instalação**:
Você pode instalar Pillow usando pip:
    
    ```bash
    pip install Pillow
    ```
    
2. **Configuração do modelo**:
Ao trabalhar com imagens em Django, você geralmente as armazena em um campo de modelo. Para isso, você deve usar o campo `ImageField`. Por exemplo:

```python
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
```

1. **Manipulação de Imagens**:
Uma vez que você tenha a imagem carregada, pode usar as funcionalidades do Pillow para manipulá-la. Por exemplo, para redimensionar uma imagem:

```python
from PIL import Image
from django.core.files.base import ContentFile

def process_image(image_file):
    image = Image.open(image_file)
    image = image.resize((800, 800))  # Redimensiona a imagem para 800x800
    image_io = BytesIO()
    image.save(image_io, format='JPEG')
    return ContentFile(image_io.getvalue(), name=image_file.name)
```

1. **Exibição de Imagens**:
No Django, você pode exibir imagens em seus templates usando a URL do campo `ImageField`:

```html
<img src="{{ my_model.image.url }}" alt="My Image">
```

[Documentação PIllow](https://pillow.readthedocs.io/en/stable/index.html)

---

## Django Filter

O **Django Filter** é uma biblioteca que facilita a filtragem de dados em consultas do Django, especialmente quando se trabalha com formulários de busca ou interfaces de usuário que exigem seleção de critérios de filtragem.

### Principais Características

1. **Filtragem Simples**: Permite que você crie filtros facilmente para modelos do Django, usando um sistema de formulários para gerenciar entradas do usuário.
2. **Integração com Django**: A biblioteca se integra perfeitamente com o Django ORM (Object-Relational Mapping), permitindo consultas dinâmicas baseadas nos filtros fornecidos pelo usuário.
3. **Suporte a Vários Tipos de Campos**: O Django Filter oferece suporte a diferentes tipos de campos de entrada, como campos de texto, seletores de data, caixas de seleção, entre outros.
4. **Customização**: Você pode personalizar o comportamento dos filtros, definindo opções como validação, formatação e apresentação.
5. **Compatibilidade com Views Baseadas em Classe**: A biblioteca pode ser usada facilmente com views baseadas em classe do Django, simplificando o processo de criação de interfaces de filtragem.

### Exemplo de Uso

Aqui está um exemplo básico de como usar o Django Filter:

1. **Instalação**:
Primeiro, você precisa instalar a biblioteca:
    
    ```bash
    pip install django-filter
    
    ```
    
2. **Configuração**:
Adicione `'django_filters'` à lista de `INSTALLED_APPS` em seu arquivo `settings.py`.
3. **Criar um Filtro**:
Defina um filtro para um modelo. Por exemplo, considere um modelo chamado `Produto`:
    
    ```python
    from django_filters import rest_framework as filters
    from .models import Produto
    
    class ProdutoFilter(filters.FilterSet):
        class Meta:
            model = Produto
            fields = {
                'preco': ['lt', 'gt'],  # Menor que e maior que
                'categoria': ['exact'],  # Igual
            }
    
    ```
    
4. **Usar o Filtro em uma View**:
Você pode aplicar o filtro em uma view:
    
    ```python
    from django.shortcuts import render
    from .models import Produto
    from .filters import ProdutoFilter
    
    def lista_produtos(request):
        produto_filter = ProdutoFilter(request.GET, queryset=Produto.objects.all())
        return render(request, 'lista_produtos.html', {'filter': produto_filter})
    
    ```
    
5. **Renderizar no Template**:
No seu template, você pode renderizar os filtros:
    
    ```html
    <form method="get">
        {{ filter.form.as_p }}
        <button type="submit">Filtrar</button>
    </form>
    
    <ul>
        {% for produto in filter.qs %}
            <li>{{ produto.nome }} - {{ produto.preco }}</li>
        {% endfor %}
    </ul>
    
    ```
    
### Conclusão

O Django Filter é uma ferramenta poderosa para simplificar a filtragem de dados em aplicações Django, tornando mais fácil para os desenvolvedores criar interfaces de busca e filtragem ricas e intuitivas. Ele economiza tempo e esforço ao lidar com a construção de consultas dinâmicas e a validação de dados de entrada.

[Documentação Django Filter](https://django-filter.readthedocs.io/en/stable/guide/usage.html)
