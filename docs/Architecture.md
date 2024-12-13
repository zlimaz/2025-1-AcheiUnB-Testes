# Arquitetura do Sistema - AcheiUnB

## Introdução

O **AcheiUnB** é um sistema de achados e perdidos voltado para estudantes da UnB. O objetivo é facilitar a localização e recuperação de itens perdidos, fornecendo uma plataforma web onde os usuários podem registrar e buscar itens que foram encontrados ou esquecidos. Este documento descreve a arquitetura do sistema, abordando os principais componentes e a interação entre eles.

## Diagrama de Arquitetura

![image protótipo](https://github.com/user-attachments/assets/5cad065a-cd23-4073-bf97-a33d7874638a)

---

## Componentes Principais

O sistema é dividido em três camadas principais:

1. **Front-end**
2. **Back-end**
3. **Banco de Dados**

Cada uma dessas camadas possui subcomponentes específicos, conforme descrito a seguir.

### 1. Front-end

- **Client (Web)**: O front-end é responsável por fornecer a interface do usuário (UI), permitindo que os usuários interajam com o sistema. No AcheiUnB, o cliente web é responsável por permitir que os usuários registrem, visualizem e busquem itens perdidos. O design e a interface são desenvolvidos utilizando **Figma**, bibliotecas CSS e frameworks para estilização e responsividade. Além disso, **Prettier** é utilizado para manter a consistência do código front-end.

### 2. Back-end

A camada de back-end é onde a lógica de negócio reside. Ela gerencia as requisições feitas pelo front-end e acessa o banco de dados para fornecer dados ou salvar novas informações. O back-end é dividido nos seguintes subcomponentes:

- **API**: A API expõe endpoints para que o front-end possa interagir com o sistema. É responsável por receber e processar as requisições do cliente web.
  - **Users**: Gerencia informações de usuários, autenticação e autorização.
  - **Search**: Lida com a busca de itens perdidos, permitindo que os usuários filtrem e encontrem itens específicos.
  - **Items**: Gerencia o registro e as atualizações dos itens de achados e perdidos, incluindo detalhes sobre o item e o status.

- **Django**: O framework principal do sistema, responsável por gerenciar as requisições HTTP, lógica de autenticação e rotas de API. Django é utilizado para orquestrar as chamadas aos módulos da API e coordenar o acesso ao banco de dados.

- **Celery**: Ferramenta de execução de tarefas assíncronas que lida com processos em segundo plano, como envio de notificações aos usuários quando um item correspondente ao seu interesse é registrado no sistema.

### 3. Banco de Dados

- **PostgreSQL**: O banco de dados utilizado para armazenar informações sobre usuários, itens e registros de achados e perdidos. Todas as interações com o banco de dados são gerenciadas pelo Django ORM, que abstrai as consultas e mantém a segurança e integridade dos dados.

---

## Tecnologias Utilizadas

O sistema utiliza uma variedade de tecnologias para garantir escalabilidade, modularidade e facilidade de manutenção:

- **DevOps**:
  - **Docker**: Docker é utilizado para containerizar o back-end, facilitando a implantação e a gestão de dependências em ambientes diferentes.
  - **GitHub Actions**: Ferramenta, disponibilizada pro próprio GitHub, que utilizada para criação das Pipelines de CI/CD, visando uma testagem automazida de todo código empurrado ao projeto por meio de scripts de workflow.
  - **CodeCov**: Plataforma online de relatório de testagem de código, utilizada para gerar gráficos de acompanhamento e sugestão de melhoria na testagem de código do software. Funciona conectando o repositório à uma conta na plataforma e enviando os relatórios dos teste gerados pela pipeline CI/CD.
  - 

- **Design/Front-end**:
  - **Figma**: Ferramenta de design utilizada para criar protótipos e garantir uma UI consistente.
  - **Bibliotecas CSS**: Utilizadas para estilizar a aplicação e garantir que a interface seja responsiva e fácil de usar.
  - **Tailwind CSS**: Um framework de CSS utilitário que permite construir estilos diretamente no HTML com classes pré-definidas, promovendo agilidade e consistência no design.
  - **Vue.js**: Um framework JavaScript progressivo para construir interfaces de usuário, focado em reatividade, modularidade e simplicidade.
  - **Vite**: Um bundler moderno e rápido para desenvolvimento front-end. Utilizado para integração do front com o back. Oferece build otimizado e HMR (Hot Module Replacement) instantâneo, tornando o desenvolvimento com Vue (e outros frameworks) mais ágil. 
  - **Prettier**: Ferramenta de formatação de código para garantir consistência no código front-end.

- **Back-end**:
  - **Django**: Framework web em Python, escolhido pela sua robustez e capacidade de integração com o PostgreSQL.
  - **Celery**: Utilizado para gerenciar tarefas assíncronas, como envio de notificações.
  - **PostgreSQL**: Banco de dados relacional utilizado para armazenamento de dados, garantindo confiabilidade e segurança.

---

## Fluxo de Dados e Comunicação

1. **Interação do Usuário com o Front-end**: O usuário acessa o **Client (Web)** para visualizar, registrar ou buscar itens perdidos. A interface foi projetada para ser intuitiva e fácil de navegar.

2. **Requisições para a API**: O **Client (Web)** envia requisições para a **API** no back-end para realizar operações, como registro de itens, atualização de informações de usuário, ou busca de itens.

3. **Processamento de Lógica de Negócio no Back-end**: A **API** processa a requisição e, se necessário, consulta ou salva informações no banco de dados. O **Django** gerencia essa comunicação, enquanto **Celery** executa tarefas assíncronas.

4. **Acesso ao Banco de Dados**: O **Django** se conecta ao **PostgreSQL** para acessar ou armazenar dados. Todo o fluxo de dados entre a API e o banco de dados é gerenciado através do ORM do Django, o que facilita a manipulação de dados e mantém a integridade das transações.

5. **Execução de Tarefas Assíncronas**: Em caso de tarefas que não precisam ser concluídas imediatamente (por exemplo, envio de notificações), **Celery** executa essas operações em segundo plano.

6. **Gerenciamento com Docker**: Todo o back-end está containerizado usando **Docker**, permitindo fácil implantação e isolamento de dependências.
---

## Conclusão

A arquitetura do AcheiUnB foi desenvolvida para ser modular, escalável e de fácil manutenção, utilizando tecnologias amplamente adotadas no mercado. Com o uso do Django, PostgreSQL e Docker, o sistema é robusto o suficiente para suportar o volume de usuários esperado e flexível para evoluir conforme a necessidade dos usuários. A separação clara entre front-end, API e banco de dados permite um desenvolvimento colaborativo eficiente e facilita a futura expansão da plataforma.
