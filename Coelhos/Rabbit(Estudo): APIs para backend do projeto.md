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


