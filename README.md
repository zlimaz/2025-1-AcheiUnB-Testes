# AcheiUnB

AcheiUnB é um projeto desenvolvido para facilitar a vida dos estudantes da Universidade de Brasília (UnB) na busca e recuperação de itens perdidos. A plataforma permite que os alunos registrem e encontrem objetos, facilitando o contato entre quem perdeu e encontrou o item. O objetivo é reduzir a dependência de grupos de mensagens e proporcionar um sistema mais organizado e acessível para achados e perdidos.

## 📝 Sumário

- AcheiUnB
  - 📝 Sumário
  - 👥 Equipe
  - ✨ Início
    - 📋 Pré-requisitos
    - 💻 Ambiente
    - 📁 Dependências do Projeto
    - 💾 Execução
      - Observações do Docker
    - ✅ Autenticação com o Google OAuth
    - 📥 Atualização do Banco de Dados
    - 🖱️ Acesso aos Serviços
    - 📍 Migrations
  - 📚 Documentação
  - 📎 Extra
    - Story Map e Activity Flow
    - Arquitetura
    - Protótipo

## 👥 Equipe

| <img src="https://github.com/anaelisaramos.png" width="150"> <br> [**Ana Elisa Marques**](https://github.com/anaelisaramos) | <img src="https://github.com/DaviCamilo23.png" width="150"> <br> [**Davi Camilo Menezes**](https://github.com/DaviCamilo23) | <img src="https://github.com/potatoyz908.png" width="150"> <br> [**Euller Júlio da Silva**](https://github.com/potatoyz908) |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://github.com/leoramiroo.png" width="150"> <br> [**Leonardo Ramiro Alves de Oliveira**](https://github.com/leoramiroo) | <img src="https://github.com/pedroeverton217.png" width="150"> <br> [**Pedro Everton de Paula**](https://github.com/pedroeverton217) | <img src="https://github.com/314dro.png" width="150"> <br> [**Pedro Henrique Martins Silva**](https://github.com/314dro) |
| <img src="https://github.com/TiagoBalieiro.png" width="150"> <br> [**Tiago Antunes Balieiro**](https://github.com/TiagoBalieiro) |  |  |



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

Para acessar o Story Map e Activity Flow, [clique aqui](https://github.com/unb-achei/2024-2-AcheiUnB/wiki/Story-Map).

### Arquitetura

A descrição da arquitetura do projeto pode ser encontrada [aqui](https://github.com/unb-achei/2024-2-AcheiUnB/wiki/Arquitetura).

### Protótipo

O protótipo da plataforma está disponível [aqui](https://github.com/unb-achei/2024-2-AcheiUnB/wiki/Protótipo).

---

AcheiUnB é um software livre, disponível sob a licença MIT.
```
