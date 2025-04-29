# Configurar notificações assíncronas usando Django Channels

**Introdução ao Django Channels**

- O **Django Channels** é uma extensão do Django que permite a comunicação em tempo real e a gestão de conexões assíncronas, algo que o Django tradicionalmente não lida bem.
- Com o Channels, você pode implementar funcionalidades como notificações em tempo real, chats ao vivo, e atualizações automáticas de dados na tela sem a necessidade de atualização da página.

**Configuração Básica do Django Channels**

- Para usar o Django Channels, é necessário instalar alguns pacotes e configurar o projeto para trabalhar com o protocolo WebSocket. Abaixo estão as instruções básicas:
    - **Instale o Django Channels**:
        
        ```bash
        pip install channels
        
        ```
        
    - **Atualize as configurações do Django**:
    No seu arquivo `settings.py`, adicione o Channels ao `INSTALLED_APPS` e configure o **ASGI** para substituí-lo como o gerenciador de servidor:
        
        ```python
        INSTALLED_APPS = [
            # Outros aplicativos
            'channels',
        ]
        
        ASGI_APPLICATION = 'seu_projeto.asgi.application'
        
        ```
        
    - **Configure o Redis como backend para Channels**:
    O Redis é popular para gerenciar sessões de WebSocket e filas de mensagens com Channels. Para isso:
        1. **Instale o Redis**:
            
            ```bash
            pip install channels_redis
            
            ```
            
        2. **Atualize as configurações**:
        No `settings.py`, configure o backend do Channels para utilizar Redis:
            
            ```python
            CHANNEL_LAYERS = {
                'default': {
                    'BACKEND': 'channels_redis.core.RedisChannelLayer',
                    'CONFIG': {
                        'hosts': [('127.0.0.1', 6379)],
                    },
                },
            }
            
            ```
            
    - **Crie um arquivo `asgi.py`**:
    Este arquivo define o **ASGI** (Asynchronous Server Gateway Interface), que o Django Channels utiliza para suportar WebSockets:
        
        ```python
        import os
        from django.core.asgi import get_asgi_application
        from channels.routing import ProtocolTypeRouter, URLRouter
        from channels.auth import AuthMiddlewareStack
        import seu_app.routing
        
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
        
        application = ProtocolTypeRouter({
            'http': get_asgi_application(),
            'websocket': AuthMiddlewareStack(
                URLRouter(
                    seu_app.routing.websocket_urlpatterns
                )
            ),
        })
        
        ```
        
1. **Configurando Tarefas Assíncronas com Celery**
    - O **Celery** é uma ferramenta poderosa para lidar com tarefas assíncronas. Ele permite o agendamento de tarefas de forma paralela e é útil para lidar com operações de notificação em tempo real.
        - **Instale o Celery**:
            
            ```bash
            pip install celery
            
            ```
            
        - **Configure o Celery no Django**:
        No `settings.py`, defina a configuração de backend do Celery para o Redis (já configurado para o Channels):
            
            ```python
            CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
            CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
            
            ```
            
            Em seguida, crie um arquivo `celery.py` no diretório principal do projeto para configurar a instância do Celery:
            
            ```python
            from __future__ import absolute_import, unicode_literals
            import os
            from celery import Celery
            
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
            
            app = Celery('seu_projeto')
            app.config_from_object('django.conf:settings', namespace='CELERY')
            app.autodiscover_tasks()
            ```
            

---

### Introdução ao Django Channels, Celery e Redis para Tarefas Assíncronas e Comunicação em Tempo Real

---

### **1. Configuração do Django Channels**

- **Introdução ao Channels para Comunicação em Tempo Real**
    - O Django Channels permite adicionar funcionalidades de comunicação em tempo real a aplicações Django, possibilitando eventos como chat ao vivo, atualizações instantâneas e notificações.
- **Configuração e Uso Básico**
    - Passos iniciais para instalação e configuração do Django Channels, incluindo definição de WebSockets e integração com o Django.

![image.png](https://images.ctfassets.net/ee3ypdtck0rk/1VuBus1RpboyS49sN9VEli/abd96f76593d5d92054260dbb40b8561/django-channels-generic-architecture-overview.png?w=1840&h=744&q=80&fm=png)

---

### **2. Configuração do Celery**

- **Instalação e Configuração do Celery para Tarefas Assíncronas**
    - O Celery é uma ferramenta poderosa para gerenciamento de tarefas assíncronas. Ele facilita o processamento de tarefas em segundo plano, ideal para operações demoradas, como processamento de dados e envio de emails.
- **Integração do Celery com Django**
    - Passo a passo para integrar o Celery com o Django, incluindo criação de tarefas e teste de execução.

![image.png](https://thetldr.tech/content/images/2021/08/image-1.png)

---

### **3. Integração do Redis com Django e Celery**

- **Instalação do Redis e Configuração como Broker para o Celery**
    - Redis é um banco de dados em memória que serve como “broker” para o Celery, gerenciando as filas de mensagens entre tarefas assíncronas.
- **Testes e Exemplos de Notificações Assíncronas**
    - Demonstrações de uso prático do Redis e Celery para enviar notificações e mensagens em tempo real, complementando a configuração com Django Channels.
    
    ![image.png](https://miro.medium.com/v2/resize:fit:1102/1*FNOoJykIEq65hnIpWzRvmg.png)
    

---

# Configuração e Uso de Signals no Django

## Introdução ao Conceito de Signals no Django

Signals são ferramentas úteis no Django para permitir que certos componentes da aplicação se comuniquem entre si, especialmente quando queremos que uma ação em um modelo desencadeie automaticamente outra ação em outra parte do sistema.

Por exemplo, podemos utilizar signals para enviar notificações ou atualizar dados sempre que determinado evento ocorrer, como a criação ou atualização de um objeto.

![image.png](https://miro.medium.com/v2/resize:fit:1400/1*3vwP83CAZIIr5_wDjSHUhg.png)

## Criação de Signals Personalizados e Conexão com Modelos

No Django, podemos criar signals personalizados que se conectam a eventos específicos dos modelos. Os signals são definidos em arquivos específicos e devem ser "conectados" a funções que realizarão as ações necessárias. Algumas das ações comuns são o envio de mensagens de confirmação de cadastro, notificações para alterações em campos específicos, entre outros.

### Passos para Configuração de um Signal:

1. Criar um arquivo de signals na aplicação desejada.
2. Definir o signal com as ações específicas que ele deve executar.
3. Conectar o signal ao evento específico do modelo (como `post_save`, `pre_delete`).
4. Configurar o arquivo `apps.py` para registrar os signals.

![image.png](https://miro.medium.com/v2/resize:fit:1400/1*qPGrT7NWzDuOiabfswEbXg.png)

# Exemplo de Automação com Notificações

![image.png](https://notificacoesinteligentes.com/wp-content/uploads/2024/01/sbswqvv475y5dxsxbebhsw5jqx71kbmm-1024x585.webp)

## Automatização de Envio de Notificações ou Atualizações com Signals

Os signals são amplamente utilizados para automatizar o envio de notificações ou atualizações de dados no sistema. Por exemplo, ao criar um novo usuário, podemos configurar um signal para enviar automaticamente uma mensagem de boas-vindas ou gerar um log de atividade.

### Exemplo Prático:

No projeto, um signal pode ser configurado para enviar uma notificação por e-mail sempre que um novo post é criado ou quando um comentário é adicionado a um artigo. Essa abordagem permite manter a comunicação entre partes do sistema sem a necessidade de chamadas explícitas e manuais.

Este exemplo ajuda a compreender como os signals facilitam a automação de tarefas e mantém o código organizado, evitando repetição de lógica em múltiplas partes do sistema.

### Materiais de Referência

1. [**Django Channels Documentation**](https://channels.readthedocs.io/en/stable/): Guia oficial do Django Channels para entender melhor a arquitetura, a configuração e exemplos de uso prático.
2. [**Celery Documentation**](https://docs.celeryproject.org/): Documentação oficial do Celery, com detalhes sobre a instalação, configuração e uso com Django.
3. [**Configuração de Redis para Django e Celery**](https://realpython.com/asynchronous-tasks-with-django-and-celery/): Um guia detalhado sobre como configurar o Redis como backend de mensagens para o Django Channels e o Celery, facilitando a comunicação entre tarefas assíncronas.
4. [Django Channels Documentation](https://channels.readthedocs.io/en/stable/) - Documentação oficial do Django Channels, com guias de configuração e exemplos práticos.
5. [Celery Documentation](https://docs.celeryproject.org/) - Guia detalhado do Celery, incluindo integração com Django e configurações avançadas.
6. [Documentação do Django sobre Signals](https://docs.djangoproject.com/en/4.0/topics/signals/)
