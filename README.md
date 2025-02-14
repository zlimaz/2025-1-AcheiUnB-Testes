# AcheiUnB

![GitHub Repo stars](https://img.shields.io/github/stars/unb-mds/2024-2-AcheiUnB?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/unb-mds/2024-2-AcheiUnB)
![Python](https://img.shields.io/badge/Python-3.12.9-blue)
![Django](https://img.shields.io/badge/Django-5.1.4-green)
![Vue.js](https://img.shields.io/badge/Vue.js-3.5.12-brightgreen)
![Docker](https://img.shields.io/badge/Docker-27.2.0-blue)
![GitHub](https://img.shields.io/github/license/unb-mds/2024-2-AcheiUnB)
![GitHub closed issues](https://img.shields.io/github/issues-closed/unb-mds/2024-2-AcheiUnB)
![GitHub closed PRs](https://img.shields.io/github/issues-pr-closed/unb-mds/2024-2-AcheiUnB)

AcheiUnB é um projeto desenvolvido para facilitar a vida dos estudantes da Universidade de Brasília (UnB) na busca e recuperação de itens perdidos. A plataforma permite que os alunos registrem e encontrem objetos, facilitando o contato entre quem perdeu e encontrou o item. O objetivo é reduzir a dependência de grupos de mensagens e proporcionar um sistema mais organizado e acessível para achados e perdidos.


## 📝 Sumário

- [AcheiUnB](#acheiunb)
  - [📝 Sumário](#-sumário)
  - [👥 Equipe](#-equipe)
  - [✨ Início](#-início)
    - [📋 Pré-requisitos](#-pré-requisitos)
    - [💾 Execução](#-execução)
      - [Observações do Docker](#observações-do-docker)
    - [✅ Autenticação com o Microsoft MSAL](#-autenticação-com-o-microsoft-msal)
    - [🖱️ Acesso aos Serviços](#️-acesso-aos-serviços)
    - [⚙️ Fluxo do Front-End](#️-fluxo-do-front-end)
    - [📚 Documentação](#-documentação)
  - [📎 Extra](#-extra)
    - [Story Map e Activity Flow](#story-map-e-activity-flow)
    - [Arquitetura](#arquitetura)
    - [Protótipo](#protótipo)

## 👥 Equipe

| [![Ana Elisa Ramos](https://avatars.githubusercontent.com/u/78448515?v=4)](https://github.com/anaelisaramos) | [![Davi Camilo Menezes](https://avatars.githubusercontent.com/u/144080784?v=4)](https://github.com/DaviCamilo23) | [![Euller Júlio da Silva](https://avatars.githubusercontent.com/u/125329742?v=4)](https://github.com/potatoyz908) | [![Leonardo Ramiro Alves de Oliveira](https://avatars.githubusercontent.com/u/144712954?v=4)](https://github.com/leoramiroo) |
|-------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Ana Elisa Marques | Davi Camilo Menezes | Euller Júlio da Silva | Leonardo Ramiro Alves de Oliveira |

| [![Pedro Everton de Paula](https://avatars.githubusercontent.com/u/117595816?v=4)](https://github.com/pedroeverton217) | [![Pedro Henrique Martins Silva](https://avatars.githubusercontent.com/u/142694744?v=4)](https://github.com/314dro) | [![Tiago Antunes Balieiro](https://avatars.githubusercontent.com/u/143669941?v=4)](https://github.com/TiagoBalieiro) | 
|-------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Pedro Everton de Paula | Pedro Henrique Martins Silva | Tiago Antunes Balieiro |


## ✨ Início

Clone o repositório do projeto usando o seguinte comando:

```bash
git clone https://github.com/unb-mds/2024-2-AcheiUnB.git
```

### 📋 Pré-requisitos

Para rodar o projeto, você precisa das seguintes ferramentas:

- **Docker** v27.2.0

### 💾 Execução

Para iniciar o projeto, use o comando:

```bash
make run
```

ou utilize os seguintes comandos:

```bash
cd API/
```

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

### ✅ Autenticação com o Microsoft MSAL

Para ativar o login com a Microsoft, substitua Client ID e Client Secret no arquivo API/.env pelo Client ID do seu projeto pelo seu token da Azure:

1. Acesse o portal do [Azure Active Directory](https://portal.azure.com/).
2. Crie um aplicativo para o AcheiUnB.
3. Defina como tipo de aplicativo "Aplicativo Web" e adicione http://localhost:8000 como origem autorizada e URI de redirecionamento.
4. Copie o Client ID e o Client Secret gerados. e substitua em API/.env.

Após a configuração, o login estará habilitado.

### 🖱️ Acesso aos Serviços

| Serviço    | URL                     |
|------------|--------------------------|
| Frontend   | http://localhost:5173    |
| Backend    | http://localhost:8000    |

### ⚙️ Fluxo do Front-End

Acesse a pasta do frontend:

```bash
cd web
```

Instale as dependências do projeto utilizando o npm:

```bash
npm install
```

Para rodar o projeto em modo de desenvolvimento:

```bash
npm run dev
```

Isso iniciará o servidor de desenvolvimento na porta `5173`.

## 📚 Documentação

Acesse a documentação completa do projeto [aqui](https://unb-mds.github.io/2024-2-AcheiUnB/).

## 📎 Extra

### Story Map e Activity Flow

Para acessar o Story Map e Activity Flow, [clique aqui](https://miro.com/app/board/uXjVLKTcaY4=/?share_link_id=775702257830).

### Arquitetura

A descrição da arquitetura do projeto pode ser encontrada [aqui](https://www.figma.com/board/ai5E0akKD2yDr9FfnW9k4l/Prot%C3%B3tipo-de-Arquitetura?node-id=0-1&t=19ErTsypFap1Nvl9-1).

### Protótipo

O protótipo da plataforma está disponível [aqui](https://www.figma.com/proto/balBSne5eGu1mDpKqEW7ey/Prot%C3%B3tipo-AcheiUnb?node-id=510-209&node-type=canvas&t=otBLAgrQGhcfPYhL-1&scaling=scale-down&content-scaling=fixed&page-id=510%3A207&starting-point-node-id=510%3A1728).

---

AcheiUnB é um software livre, disponível sob a licença MIT.
