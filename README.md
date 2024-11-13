# AcheiUnB

AcheiUnB é um projeto desenvolvido para facilitar a vida dos estudantes da Universidade de Brasília (UnB) na busca e recuperação de itens perdidos. A plataforma permite que os alunos registrem e encontrem objetos, facilitando o contato entre quem perdeu e encontrou o item. O objetivo é reduzir a dependência de grupos de mensagens e proporcionar um sistema mais organizado e acessível para achados e perdidos..

## 📝 Sumário

- [AcheiUnB](#acheiunb)
  - [📝 Sumário](#-sumário)
  - [👥 Equipe](#-equipe)
  - [✨ Início](#-início)
    - [📋 Pré-requisitos](#-pré-requisitos)
    - [💻 Ambiente](#-ambiente)
    - [📁 Dependências do Projeto](#-dependências-do-projeto)
    - [💾 Execução](#-execução)
      - [Observações do Docker](#observações-do-docker)
    - [✅ Autenticação com o Google OAuth](#-autenticação-com-o-google-oauth)
    - [📥 Atualização do Banco de Dados](#-atualização-do-banco-de-dados)
    - [🖱️ Acesso aos Serviços](#️-acesso-aos-serviços)
    - [📍 Migrations](#-migrations)
  - [📚 Documentação](#-documentação)
  - [📎 Extra](#-extra)
    - [Story Map e Activity Flow](#story-map-e-activity-flow)
    - [Arquitetura](#arquitetura)
    - [Protótipo](#protótipo)

## 👥 Equipe

| [![Ana Elisa Marques](https://avatars.githubusercontent.com/u/78448515?v=4)](https://github.com/anaelisaramos) | [![Davi Camilo Menezes](https://avatars.githubusercontent.com/u/144080784?v=4)](https://github.com/DaviCamilo23) | [![Euller Júlio da Silva](https://avatars.githubusercontent.com/u/125329742?v=4)](https://github.com/potatoyz908) | [![Leonardo Ramiro Alves de Oliveira](https://avatars.githubusercontent.com/u/144712954?v=4)](https://github.com/leoramiroo) |
|-------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Ana Elisa Marques | Davi Camilo Menezes | Euller Júlio da Silva | Leonardo Ramiro Alves de Oliveira |

| [![Pedro Everton de Paula](https://avatars.githubusercontent.com/u/117595816?v=4)](https://github.com/pedroeverton217) | [![Pedro Henrique Martins Silva](https://avatars.githubusercontent.com/u/142694744?v=4)](https://github.com/314dro) | [![Tiago Antunes Balieiro](https://avatars.githubusercontent.com/u/143669941?v=4)](https://github.com/TiagoBalieiro) | 
|-------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Pedro Everton de Paula | Pedro Henrique Martins Silva | Tiago Antunes Balieiro |


## ✨ Início

Clone o repositório do projeto usando o seguinte comando:

```bash
git clone https://github.com/unb-achei/2024-2-AcheiUnB.git
```

### 📋 Pré-requisitos

Para rodar o projeto, você precisa das seguintes ferramentas:

- **Python** v3.11.6 e **Pip** v22.0.2 ou superior

### 💻 Ambiente

Para configurar o ambiente, rode o seguinte script:

```bash
make config
```

### 📁 Dependências do Projeto

Para instalar as dependências, siga os passos abaixo:

```bash
# Crie um ambiente virtual para Python
python3 -m venv api/env

# Ative o ambiente virtual
source api/env/bin/activate

# Instale os pacotes do Python e do Node
make install
```

### 💾 Execução

Para iniciar o projeto, use o comando:

```bash
docker compose up
```

#### Observações do Docker

- Para rodar o projeto em segundo plano:

  ```bash
  docker compose up -d
  ```

- Caso precise reconstruir a imagem do Docker:

  ```bash
  docker compose up --build
  ```

- Se for necessário deletar os volumes:

  ```bash
  docker compose down -v
  ```

### ✅ Autenticação com o Google OAuth

Para ativar o login com Google, substitua `your_client_id` no arquivo `web/.env.local` pelo Client ID do seu projeto no Google Cloud:

1. Crie um projeto no [Google Cloud](https://console.cloud.google.com/).
2. Vá para "Credenciais" e selecione "Criar credenciais" > "ID do cliente OAuth".
3. Defina como tipo de aplicativo "Aplicativo Web" e adicione `http://localhost:3000` como origem autorizada e URI de redirecionamento.
4. Copie o Client ID e substitua em `web/.env.local`.

Após essa configuração:

1. No [Google Cloud](https://console.cloud.google.com/), vá para "Tela de Consentimento OAuth".
2. Adicione o seu e-mail como usuário de teste e salve.

### 📥 Atualização do Banco de Dados

Os dados são obtidos por meio de scraping do site da UnB e precisam ser atualizados periodicamente. Para atualizar, use:

```bash
make updatedb-all
```

ou, de forma equivalente:

```bash
docker exec django-api python3 ./manage.py updatedb -a
```

### 🖱️ Acesso aos Serviços

| Serviço    | URL                     |
|------------|--------------------------|
| Frontend   | http://localhost:3000    |
| Backend    | http://localhost:8000    |

### 📍 Migrations

Sempre que alterar o modelo de dados, crie novas migrations com os comandos:

```bash
make makemigrations  # Cria as migrations
make migrate         # Executa as migrations
```

## 📚 Documentação

Acesse a documentação completa do projeto [aqui](https://github.com/unb-achei/2024-2-AcheiUnB/wiki).

## 📎 Extra

### Story Map e Activity Flow

Para acessar o Story Map e Activity Flow, [clique aqui](https://miro.com/app/board/uXjVLKTcaY4=/?share_link_id=775702257830).

### Arquitetura

A descrição da arquitetura do projeto pode ser encontrada [aqui](https://www.figma.com/board/ai5E0akKD2yDr9FfnW9k4l/Prot%C3%B3tipo-de-Arquitetura?node-id=0-1&t=19ErTsypFap1Nvl9-1).

### Protótipo

O protótipo da plataforma está disponível [aqui](https://github.com/unb-achei/2024-2-AcheiUnB/wiki/Protótipo).

---

AcheiUnB é um software livre, disponível sob a licença MIT.
