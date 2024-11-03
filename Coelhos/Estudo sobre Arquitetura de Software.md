### **Pesquisa sobre Arquitetura de Software**
---
#### **O que é?**
A arquitetura de software refere-se, de maneira resumida, à abordagem adotada para gerenciar os componentes essenciais de um projeto, definidos e organizados pelos desenvolvedores.

#### **Porquê é importante?**
A arquitetura é fundamental para o desenvolvimento de software, pois, sem ela, o código pode se tornar desorganizado e confuso, o que dificulta e prolonga o processo de implementação das modificações necessárias. Quanto maior a qualidade interna do produto, mais rapidamente serão entregues as funcionalidades, assim, acelerando o desenvolvimento do software.

#### **Quem serão os Coelhos?**
Os responsáveis por apresentar a por esta tarefa serão **Pedro Silva**, @314dro e **Tiago Balieiro**, @TiagoBalieiro.

#### **Tópicos a serem estudados:**
- [x] **Documentação**
- [x] **Staks** 
- [x] **Framework**
- [x] **API**

**Estudo:**
Todas as anotações dos estudos estão na pasta [Coelhos.](https://github.com/unb-mds/2024-2-AcheiUnB/tree/main/Coelhos).

#### **Arquitetura de Software**
# Uma breve introdução sobre arquitetura de software

Após ler um artigo indicado pela professora sobre arquitetura de software, o conceito ficou bem claro para mim. A arquitetura de software é, de forma resumida, a forma como se pretende lidar com as partes importantes do projeto, definidas pelos desenvolvedores.

A arquitetura é essencial para o software, pois sem ela o código se torna poluído, fazendo com que seja mais difícil e demore mais para realizar as modificações necessárias. 🧩

[[Link para o artigo](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOws-RltPS457qsIxwp26e1jkIyJdZXYQRz7TBe2-lhjxNdPoj_MtrTTac5kigCsUwQ-yX2BsISuEMlwS6zx9-EskvcJy3v_ytq1MOqmr5VI2unW0HuUQAcp01NCU6zG9WH4YsyqaIBikY8XxSFE-4i4EI?key=zaDTgrjPjKgjBEz7mlb2b-Vn)](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOws-RltPS457qsIxwp26e1jkIyJdZXYQRz7TBe2-lhjxNdPoj_MtrTTac5kigCsUwQ-yX2BsISuEMlwS6zx9-EskvcJy3v_ytq1MOqmr5VI2unW0HuUQAcp01NCU6zG9WH4YsyqaIBikY8XxSFE-4i4EI?key=zaDTgrjPjKgjBEz7mlb2b-Vn)

Quanto maior a qualidade interna do produto, mais rápido serão entregues os *features*, acelerando o processo de desenvolvimento. 🏃‍♂️💻

**“Attention to internal quality pays off in weeks, not months.”** ⏳

A arquitetura de software é algo que até mesmo os melhores arquitetos vão aprendendo durante os projetos.

“We made good decisions, but only now do we understand how we should have built it.”

[[Martin Fowler sobre arquitetura](https://martinfowler.com/architecture/)](https://martinfowler.com/architecture/)

## **Documentação** 📄

### **Documento de Visão**

O documento de visão em um projeto de software é idealizado pelo time de desenvolvedores para os *stakeholders*. Ele descreve o propósito do projeto, os problemas que ele resolve, os principais objetivos e o custo para os usuários e para o negócio. Esse documento ajuda a alinhar expectativas e guiar o desenvolvimento. 📊

Componentes principais:

1. **Introdução**: contexto, objetivos, escopo, público-alvo.
2. **Problema**: descrição da oportunidade que o projeto aborda.
3. **Objetivos e Sucesso**: critérios para medir o sucesso do sistema.
4. **Stakeholders**: identificação de clientes, usuários, equipe técnica.
5. **Requisitos de alto nível**: principais funcionalidades do sistema.
6. **Restrições e Premissas**: fatores que limitam o desenvolvimento.
7. **Riscos**: principais riscos identificados.

[[Exemplo de Documento de Visão](https://prodest.es.gov.br/Media/prodestnovo/UECI/Exclusiva/ANEXO%20I%20-%20Modelo%20de%20Documento%20de%20Vis%C3%A3o.pdf)](https://prodest.es.gov.br/Media/prodestnovo/UECI/Exclusiva/ANEXO%20I%20-%20Modelo%20de%20Documento%20de%20Vis%C3%A3o.pdf)

**TAP (Termo de Abertuda de Projeto)**

O **Termo de Abertura do Projeto (TAP)** formaliza o início do projeto, definindo objetivos, escopo, *stakeholders* e recursos necessários. Elementos comuns incluem:

1. **Objetivo do Projeto**
2. **Justificativa e Benefícios**
3. **Escopo**
4. **Stakeholders**
5. **Premissas e Restrições**
6. **Orçamento e Recursos**
7. **Cronograma**
8. **Riscos**

[[Exemplo de TAP](https://planejamentoestrategico.ifma.edu.br/wp-content/uploads/sites/53/2019/03/TA-Projeto-Estrate_gico-FABRICA-DE-INOVACAO.pdf)](https://planejamentoestrategico.ifma.edu.br/wp-content/uploads/sites/53/2019/03/TA-Projeto-Estrate_gico-FABRICA-DE-INOVACAO.pdf)

### **Documento de Arquitetura** 🏗️

Esse documento detalha a estrutura técnica e as decisões de design do sistema. Ele ajuda a manter consistência e eficiência no desenvolvimento. Componentes incluem:

1. **Visão Geral da Arquitetura**
2. **Decisões Arquiteturais**
3. **Diagrama de Arquitetura**
4. **Componentes e Módulos**
5. **Requisitos Não Funcionais**
6. **Interfaces e Comunicação**
7. **Restrições Técnicas**
8. **Estratégia de Evolução**

[[Exemplo de Documento de Arquitetura](https://datasus.saude.gov.br/wp-content/uploads/2019/12/Documento-de-arquitetura-de-software.docx)](https://datasus.saude.gov.br/wp-content/uploads/2019/12/Documento-de-arquitetura-de-software.docx)

[[Template de Documento de Arquitetura por RUP](https://www.notion.so/Arquitetura-de-Software-e3434f0456cf444ab594daecd10cb374?pvs=21)](https://www.notion.so/Arquitetura-de-Software-e3434f0456cf444ab594daecd10cb374?pvs=21)

[[Template de Documento de Arquitetura em português (UFPE)](https://cin.ufpe.br/~gta/rup-vc/extend.formal_resources/guidances/examples/resources/sadoc_v1.htm#toc)](https://cin.ufpe.br/~gta/rup-vc/extend.formal_resources/guidances/examples/resources/sadoc_v1.htm#toc)

## **Stacks (Pilha)** 🛠️

Em arquitetura de software, o termo **stack** refere-se ao conjunto de tecnologias usadas para desenvolver e executar uma aplicação.

### Principais componentes de um stack:

1. **Front-end**: tecnologias como HTML, CSS, JavaScript (React, Angular, Vue.js).
2. **Back-end**: linguagens como Java, Python, Node.js, com frameworks como Spring e Django.
3. **Banco de Dados**: MySQL, PostgreSQL, MongoDB.
4. **Servidor**: Apache, Nginx.
5. **Infraestrutura/DevOps**: Docker, Kubernetes, AWS, Jenkins.

### Importância do Stack:

Escolher o stack correto influencia diretamente a performance, escalabilidade e manutenção da aplicação.

# Frameworks

Frameworks são estruturas de software que fornecem um conjunto organizado de códigos, bibliotecas e ferramentas prontas para facilitar o desenvolvimento de aplicações. Diferente de uma biblioteca, que apenas oferece funcionalidades específicas, um framework estabelece uma base e uma arquitetura padrão, orientando a estrutura do código e a forma de desenvolver a aplicação. Ele define um “esqueleto” que o desenvolvedor preenche, implementando apenas partes específicas e focando nas regras de negócio. Exemplos de frameworks incluem Django para desenvolvimento web em Python, Spring para aplicações em Java e React para interfaces de usuário em JavaScript.

## Tipos de Frameworks

- **Frameworks Web**: Facilitam o desenvolvimento de aplicações web, fornecendo estruturas para backend e frontend. Exemplos incluem **Django** e **Flask** (backend em Python), **Spring** (backend em Java), **React** e **Angular** (frontend em JavaScript).
- **Frameworks Mobile**: São voltados para a criação de aplicativos móveis, como **React Native** e **Flutter**, que possibilitam a construção de apps multiplataforma (iOS e Android) com um único código.
- **Frameworks para Desenvolvimento Desktop**: Usados para criar aplicativos de desktop, como o **Electron** (JavaScript) e o **Qt** (C++).

## Inversão de Controle

A **Inversão de Controle (IoC)** é uma característica fundamental dos frameworks, onde o controle do fluxo da aplicação é "invertido". Em vez de o desenvolvedor decidir quando e como certos códigos são executados, o framework assume esse controle, chamando o código do desenvolvedor em pontos específicos (geralmente definidos pelo framework).

## Vantagens e desvantagens do uso de Frameworks

Vantagens:

- **Aceleram o desenvolvimento**: Ao fornecer componentes prontos e uma estrutura definida.
- **Padronizam o código**: Tornando mais fácil a colaboração entre desenvolvedores.
- **Incorporam boas práticas**: Fornecendo segurança e performance adequadas.

Desvantagens:

- **Curva de aprendizado**: Alguns frameworks são complexos e exigem conhecimento prévio.
- **Dependência**: Projetos muito dependentes de um framework específico podem ser difíceis de migrar ou atualizar no futuro.
- **Perda de flexibilidade**: Ao impor uma estrutura, frameworks podem limitar escolhas de arquitetura e desenvolvimento.

# APIs

APIs (Application Programming Interfaces) são conjuntos de regras e protocolos que permitem que diferentes sistemas ou componentes de software se comuniquem entre si. Elas funcionam como intermediárias, definindo como dados e funcionalidades podem ser solicitados e compartilhados, seja entre partes internas de uma aplicação ou entre aplicações independentes. 

Com APIs, um desenvolvedor pode integrar funcionalidades de outros serviços, como sistemas de pagamento, mapas ou redes sociais, diretamente em sua aplicação, sem precisar reescrever o código desses serviços. Um exemplo comum é o uso de APIs RESTful para criar interações entre o frontend e o backend de uma aplicação web. APIs também promovem a modularidade e a interoperabilidade, tornando o desenvolvimento de software mais eficiente e escalável.

## Tipos de APIs:

- **REST (Representational State Transfer)**: Um dos tipos mais populares, REST é baseado em HTTP e usa métodos como GET, POST, PUT e DELETE. APIs RESTful são simples de implementar e flexíveis, sendo amplamente usadas para comunicações entre sistemas web.
- **SOAP (Simple Object Access Protocol)**: Baseada em XML, SOAP é uma API mais rígida e complexa que REST, usada principalmente em sistemas corporativos que exigem alta segurança e transações confiáveis. Ela é frequentemente usada em ambientes de integração complexos e que exigem compatibilidade com sistemas legados.
- **GraphQL**: Criada pelo Facebook, GraphQL é uma alternativa ao REST que permite que os clientes escolham exatamente os dados que precisam. Isso evita o "over-fetching" (obter dados desnecessários) e o "under-fetching" (faltar dados essenciais), otimizando a performance das requisições.
- **gRPC (Google Remote Procedure Call)**: Desenvolvido pelo Google, gRPC usa o protocolo HTTP/2 e é baseado na troca de mensagens binárias para realizar chamadas de procedimento remoto. Ele é ideal para comunicação em tempo real e sistemas de alta performance, como microserviços.

## **Protocolos de Comunicação**

APIs utilizam diversos protocolos de comunicação para enviar e receber dados:

- **HTTP (Hypertext Transfer Protocol)**: Amplamente usado em APIs REST, HTTP é um protocolo de comunicação de texto que facilita a interação entre sistemas por meio de métodos (GET, POST, etc.) e é facilmente integrável com a web.
- **HTTPS (HTTP Secure)**: Versão segura do HTTP, o HTTPS adiciona uma camada de criptografia SSL/TLS, garantindo que a troca de dados entre cliente e servidor seja confidencial. A maioria das APIs modernas exige HTTPS para proteger as informações transmitidas.
- **WebSocket**: Um protocolo de comunicação bidirecional que permite que o servidor envie dados para o cliente sem que o cliente precise fazer uma nova solicitação. Muito usado para aplicações em tempo real, como chats e atualizações em tempo real de dados.
- **AMQP (Advanced Message Queuing Protocol)**: Embora menos comum em APIs para a web, é um protocolo utilizado para filas de mensagens e é popular em sistemas que necessitam de alta confiabilidade e baixa latência.

# Figma

Ao contrário do que muitos acreditam, Figma não é um framework. Ele é uma ferramenta de design colaborativo, onde diversas pessoas podem trabalhar ao mesmo tempo no mesmo aquivo. Ele é voltado principalmente para criação de interfaces de usuário (UI) e experiências de usuário (UX). O Figma permite que seus usuários criem protótipos interativos e desenvolvam layouts de alta fidelidade que podem ser testados e compartilhados em tempo real com outras equipes.

![https://cdn.prod.website-files.com/59e16042ec229e00016d3a66/64309f16d7ce84563bc2c254_Slide%201%20(43).webp](https://cdn.prod.website-files.com/59e16042ec229e00016d3a66/64309f16d7ce84563bc2c254_Slide%201%20(43).webp)
