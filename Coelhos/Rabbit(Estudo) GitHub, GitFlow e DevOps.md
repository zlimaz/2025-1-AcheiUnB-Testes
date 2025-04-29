
# DevOps

## Introdução ao DevOps

O DevOps é uma cultura e um conjunto de práticas que unem desenvolvimento (Dev) e operações (Ops) para automatizar e integrar processos de desenvolvimento de software.

O objetivo é melhorar a colaboração entre equipes, aumentar a eficiência e entregar software com mais qualidade e rapidez.

## Por que DevOps é importante?

Com a demanda crescente por entregas ágeis e frequentes, as empresas precisam responder rapidamente às mudanças de mercado e às necessidades dos clientes.

DevOps facilita uma integração contínua e entrega contínua (CI/CD), o que resulta em ciclos de desenvolvimento mais curtos e feedback mais rápido.

## Principais práticas e ferramentas

Automação: Prática de reduzir processos manuais em toda a cadeia de desenvolvimento, integração e implantação, usando scripts, pipelines de CI/CD e ferramentas de configuração. A automação permite maior consistência, acelera entregas e minimiza erros humanos em cada etapa.

Integração Contínua (CI): Prática de automatizar testes e validações sempre que há novas alterações no código.

Entrega Contínua (CD): Processo de entregar software pronto para produção de forma automatizada.

Infraestrutura como Código (IaC): Permite gerenciar e provisionar infraestrutura por meio de scripts, tornando o processo mais ágil e repetível.

Microsserviços: Prática de desenvolver sistemas como uma coleção de pequenos serviços independentes e especializados, de forma que caso alguma funcionalidade "quebre" ela consiga ser isolada para não "quebrar" todo o sistema junto.

Monitoramento e Feedback: Monitoramento contínuo para identificar problemas rapidamente e implementar melhorias com base no feedback do usuário, utilizando por exemplo sistemas de logs.

## Benefícios de adotar DevOps

Agilidade e Velocidade: Com práticas de Integração Contínua (CI) e Entrega Contínua (CD), as equipes conseguem automatizar testes e integrações, reduzindo o tempo para colocar novas funcionalidades em produção. Por exemplo, em vez de esperar semanas para lançar uma nova versão, podemos implementar atualizações menores e frequentes, liberando novas funcionalidades semanalmente ou até diariamente.

Confiabilidade: A automação em DevOps permite realizar testes automáticos em cada alteração do código, o que ajuda a identificar erros logo no início. Com isso, em vez de os problemas surgirem apenas em produção, eles são detectados e corrigidos já nas fases iniciais do desenvolvimento. Um exemplo é a prática de testes automatizados em pipelines de CI/CD, onde todo novo código passa por uma série de validações antes de ir para produção.

Escalabilidade: Ferramentas de Infraestrutura como Código (IaC), como Terraform ou Ansible, permitem criar e gerenciar ambientes de infraestrutura automaticamente. Se a empresa precisar de mais servidores ou de novos ambientes para suportar um aumento de usuários, podemos escalá-los automaticamente usando scripts, sem necessidade de configurações manuais. Isso facilita responder a picos de demanda, como promoções ou eventos sazonais.

Colaboração: A implementação de práticas e ferramentas DevOps, como uso de repositórios compartilhados, pipelines de CI/CD e monitoramento integrado, reduz barreiras entre as equipes de desenvolvimento e operações. Por exemplo, os desenvolvedores têm acesso a ferramentas que antes eram exclusivas do time de operações, podendo colaborar para resolver incidentes e melhorar processos juntos, o que agiliza a resposta a problemas.

Esses exemplos mostram como o DevOps traz benefícios práticos e concretos, ajudando a empresa a operar de forma mais ágil, confiável e colaborativa.

## Impacto no negócio

A adoção de DevOps aumenta a competitividade e a satisfação do cliente, pois permite responder rapidamente a mudanças de mercado e melhorar a experiência de uso.

Em resumo, DevOps não é apenas uma metodologia técnica, mas um diferencial estratégico.

## Links interessantes

https://aws.amazon.com/pt/devops/what-is-devops/

https://www.atlassian.com/br/devops

https://engsoftmoderna.info/cap10.html

# FUNCIONALIDADES DO GITHUB

O **GitHub** é uma ferramenta essencial para o desenvolvimento de softwares, especialmente em equipes, pois oferece as funcionalidades necessárias para a colaboração em projetos. Entre suas principais características, destaca-se o controle de versões, que permite rastrear e reverter alterações de código de maneira eficiente. O gerenciamento de **branches** possibilita que os desenvolvedores trabalhem em diferentes funcionalidades simultaneamente, sem interferir no código principal. Os **pull requests** facilitam a revisão e a integração dessas mudanças, garantindo que o código compartilhado seja de alta qualidade.

Além disso, as **issues** servem como um sistema de rastreamento de tarefas, permitindo que as equipes identifiquem e priorizem problemas e novas funcionalidades de forma organizada. A automação de processos com **GitHub Actions** também é um recurso importante, permitindo a execução de testes e a implementação contínua, o que melhora a eficiência do ciclo de desenvolvimento. Com essas ferramentas, o GitHub não só melhora a colaboração, mas também aumenta a produtividade e a qualidade do software desenvolvido em equipe.

## Funcionalidades do Git e GitHub para Desenvolvimento de Software

## 1. Versionamento de Código com Git (Gerenciar versões de um código)

- **O que é**: O **Git** é um sistema de controle de versão que permite rastrear mudanças no código ao longo do tempo. Foi criado pelo **Linus Torvalds**, mesmo criador do Linux, um sistema operacional open source, como solução para a falta de **versionamento de código** eficiente para um projeto com a magnitude do Linux.
- **Como usar**: Use comandos como `git init, git add, git commit` para inicializar repositórios, adicionar arquivos ao índice e registrar alterações. Cada commit cria um "snapshot" do seu projeto em um determinado ponto no tempo.

![image.png](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdqOXxqi5N5C9oz4YsqvQGtayPH50C7vLs8XRQulvxG1SrMFVvdpKpuo9k6Y8GAhcSdagLTD_GKMFsvnH24VaX4I_WGeqlSame2uSQlITQJgkxMVy0U8-c4wKnkugFsq6lCCghyFcUYrHALuFxCpwLRM80c?key=U3qBmGGvsTryaoczr65frJM_)

## 2. Branches (Ramificações)

- **O que é**: **Branches** permitem que você trabalhe em **diferentes funcionalidades** ou correções de bugs **sem afetar** o código principal.
- **Como usar**: Crie uma nova branch com ``git branch [nome-da-branch]`` e mude para ela com ``git checkout [nome-da-branch]``. Quando a funcionalidade estiver pronta, você pode mesclar as mudanças na branch principal (geralmente `main` ou `master`).

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/089522da-1e53-42b1-802e-4499614c3cf2/image.png?table=block&id=0a352474-f29d-470f-8bd3-0c8a2a845c58&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730498400000&signature=2g_v-__u3-Xdeatiyb_w5hVO2e2srQU61DyPJa14YWA&downloadName=image.png)

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/f7a76d35-9ab3-4c79-bdcf-180a61802439/image.png?table=block&id=bf1e3a98-b0b8-4920-8b50-63cf98e930a2&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=-ZZEyOMznFrUPXb-79Qg5CfoQ4_pASQ60zY29_bp5aI&downloadName=image.png)
## 3. Merge (Mesclar)

- **O que é**: O merge é o processo de integrar as alterações de uma **branch** a outra.
- **Como usar**: Após a revisão de um **pull request**, você pode mesclar as alterações clicando no botão "Merge" no GitHub. Isso combina as alterações na **branch** de destino.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/52c09bb7-9342-4287-9350-d90a97a2d4cf/image.png?table=block&id=e66bccca-8069-4ae8-afdd-9e4efe3c0678&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=4-8odqYcpfqpy-owfl2vQNsMJlcsKes4RexPoCecBKU&downloadName=image.png)
## 4.Commit (Tornar real uma alteração ou conjunto delas)

- **O que é**: **Commits** são registros de alterações no código. Cada **commit** deve ter uma **mensagem clara que descreva** o que foi mudado.
- **Como usar**: Utilize o código `git commit -m "Sua mensagem aqui"` para criar um **commit** com uma descrição. Mantenha mensagens curtas e informativas.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/7f19db2b-28ab-4593-b47d-592333a4cd7d/image.png?table=block&id=d5596212-3ab3-4817-815e-1a93ad817869&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=RNOyVlpBQTxlv_R5iH1IRVhniZKGvypIHiVBx3L7jEE&downloadName=image.png)

## 5. Pull Requests (PRs) (”Proposta de alteração”)

- **O que é**: Um **pull request** é uma solicitação para mesclar mudanças de uma **branch** para outra (geralmente da sua branch de trabalho para a branch principal).
- **Como usar**: Após fazer alterações e comitar, vá para o GitHub e crie um pull request. Os revisores podem comentar, sugerir alterações e aprovar as mudanças.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/e30f40cb-aa7c-4159-a10e-c7d390be7cd2/image.png?table=block&id=e216a0b0-b2d9-4b6d-89ad-07f30e13589e&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=1x4_1yXOs8pp1CqzhKVwjfiBuH269rnGKZtonGb3CaI&downloadName=image.png)

## 6. Issues (Emitir, Publicar) 

- **O que é**: As **issues** permitem rastrear bugs, funcionalidades e tarefas. Elas ajudam a organizar e priorizar o trabalho.
- **Como usar**: Crie uma nova **issue** no GitHub para cada bug, tarefa, estudo e etc. Forneça um título e uma descrição clara, e atribua a um membro da equipe.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/11c9fb2e-f820-4782-9259-1a506d869ced/image.png?table=block&id=3015206c-122c-4db7-a865-9788b7552068&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=b78XD3rg5_K_69hJxoWGAaAmxCNMqIF_BWf0-rZD8qs&downloadName=image.png)

## 7. Milestones (Marcos)

- **O que é**: Milestones são objetivos que agrupam **issues** relacionadas a uma versão ou etapa do projeto.
- **Como usar**: Crie milestones no GitHub e associe issues a elas para acompanhar o progresso e as metas do projeto.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/e9c27e87-ee50-479e-aa3f-c12039730331/image.png?table=block&id=8e1c2dfc-720e-4c8c-94ab-17fd04fada5b&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=NoqjmyZV63ultsDj39gicXkT6z6L_V0VFDiPRUP82Hw&downloadName=image.png)

## 8. Labels (Rótulos para caracterizar issues, PRs e discussões)

- **O que é**: Labels ajudam a categorizar issues e pull requests, facilitando a visualização e o gerenciamento do trabalho.
- **Como usar**: Atribua labels (como "bug", "feature", "high priority") às suas issues para facilitar a identificação e o gerenciamento.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/5ba37f77-031b-44aa-8339-24e58cd8e60d/image.png?table=block&id=918f5db0-5bcd-431d-8ede-4a2d5928c30d&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=kkC0pVhrvQNZ5dB-ObvdZd4xXOf1j3cxi8x6V0BQ1cU&downloadName=image.png)
## 9. Fork e Clonagem (Open-source em ação)

- **O que é**: Fork é uma cópia de um repositório que permite que você faça alterações sem afetar o original. Clonagem é a ação de copiar um repositório localmente.
- **Como usar**: Use o botão "Fork" no GitHub para criar uma cópia do repositório. Para clonar, use ``git clone [url-do-repositório]``.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/48deda07-d41d-489a-a3a1-64231e6a40b4/image.png?table=block&id=442596bc-55c2-43bb-b9af-4af67c92af59&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=6bAuOTjUb1RWaD9x3LjrNTq7Yp9GIYZQNdjax4VeoFo&downloadName=image.png)

## 10. GitHub Actions

- **O que é**: GitHub Actions permite automatizar fluxos de trabalho(programar tarefas), integrações contínuas(CI)(execução de testes automáticos), Entregas contínuas(CD)(programando deploy quando aprovado) e integrações com outras ferramentas como Docker, AWS, Google Cloud e etc.
- **Como usar**: Crie arquivos de configuração YAML("Yet Another Markup Language”) no diretório `.github/workflows` para definir ações automatizadas que executam scripts, testes e deploys quando eventos específicos ocorrem, como um push para a branch principal.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/ffea7efe-aebd-4b3c-8a4d-232e15c44c6b/image.png?table=block&id=28c44050-836b-4945-84fb-b69ff299864f&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=kMr7ekMuGzGIVedGpEKoTzTtDA8RHkPpL5yYOPCr51A&downloadName=image.png)

## 11. Releases (Versão Oficial do projeto)

- **O que é**: Releases são versões estáveis do seu projeto que podem ser disponibilizadas para download.
- **Como usar**: Na aba "Releases" do seu repositório, você pode criar uma nova release, adicionando notas de versão e arquivos binários, se necessário.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/4e16af43-e5a0-4b61-954b-99ba330e1663/image.png?table=block&id=191e34a7-0670-4d2b-a788-7d7c956728de&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=bQc-cSD2XdnJnd8tMjM9nkoIwSP6cvPzpEUbwWosnY4&downloadName=image.png)

## 12. GitHub Pages (Acredito que o site da professora seja um exemplo)

- **O que é**: GitHub Pages permite **hospedar gratuitamente** sites estáticos diretamente a partir do seu repositório, tem suporte com a Jekyll(gerador de sites estáticos) usando assim layouts e templates **com ou sem back-end**.
- **Como usar**: Configure uma branch específica (geralmente ``gh-pages``) ou um diretório (como ``docs``) nas configurações do repositório para que o GitHub crie e publique o site.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/2e3a0355-4912-4876-a1c5-19590c5f0726/image.png?table=block&id=5aedee97-722f-4288-a038-0484e0eb6568&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=nhH2xfCJbLwmrOCs7oIMJ34BQMwmiwfNGdJLQc2d59g&downloadName=image.png)

## 13. Protected Branches (Branches restritos)

- **O que é**: Branches protegidas impedem que alterações sejam feitas diretamente em **branches** específicas sem revisão. Costuma ser interessante em projetos em grupo onde a **main** não deve ser modificada diretamente sem revisão ou testes adequados
- **Como usar**: Nas configurações do repositório, defina quais **branches** são **protegidas** e quais regras (como revisões obrigatórias) devem ser seguidas.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/d6213796-6503-4bf8-b350-3802886bf5a6/image.png?table=block&id=aa5902a2-a106-4d15-96d6-906d50074816&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=mAE9x93IKNUT1yeWYo_RvUDr7aH4sLJPvxfLBdhujXs&downloadName=image.png)

## 14. Code Review (Revisão de código ou projeto)

- **O que é**: Code review é o processo de revisão de código por outros membros da equipe antes da merge(mesclagem).
- **Como usar**: Ao abrir um pull request, outros colaboradores podem deixar comentários e sugestões, garantindo que o código esteja revisado e em conformidade com os padrões do projeto.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/dd21484c-0c41-4325-a991-38f740d8c62a/image.png?table=block&id=a3a28e55-c7d3-4204-86ca-e747a541cd0a&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=CSO-IUTuy-t41x7zbnVXmWxY2FhjDX5Lh662BP0LIWc&downloadName=image.png)

## 15. Documentação com Wiki (Documentação colaborativa)

- **O que é**: A Wiki do GitHub permite documentar seu projeto de forma colaborativa.
- **Como usar**: Crie páginas para tutoriais, documentação de APIs e guias de uso dentro da aba "Wiki" do seu repositório. Pode ser usado para fazer descrições longas que podem ser compartilhadas
- Contém edição simples, formato de páginas que podem ser interligadas por links internos criando assim uma estrutura de navegação contínua.

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/30c57124-419d-4899-81f6-359e6d0d55e0/image.png?table=block&id=68015173-9a02-4555-a738-9ac447e43952&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=SmVrsaMeAiv8FU4yU7lAUKzMoA8DN4Z8EmY0TDwIg-g&downloadName=image.png)

Utilizei de vários sites como githubdocs, tutoriais, alguns vídeos do youtube e imagens em geral. Hope you enjoy.

# GitFlow

## O que é?

O GitFlow se trata de um modelo alternativo de ramificação do Git que consiste no uso de ramificações de recursos e várias ramificações primárias. Em outras palavras, define-se como uma forma de controlar branches de repositórios, quando existem vários contribuidores em um projeto. No geral, o que ele faz é atribuir funções bem específicas para diferentes ramificações e definir quando elas devem interagir (workflow), facilitando, assim, o desenvolvimento compartilhado de código com pessoas desenvolvedoras, tal como a organização do versionamento de ramificações.

## Por que utilizar?

Tal método é útil para o projeto em questão, tendo em vista a recomendação de uso em projetos em que há um ciclo de lançamento agendado (uma data de entrega), e que estejam alinhados à prática de DevOps de entrega contínua. Além disso, se trata de um projeto no qual existe uma grande quantidade de pessoas “commitando” dentro de um repositório.

## Como funciona?

Sob este modelo, os desenvolvedores criam uma ramificação de recurso e retardam o merge com a ramificação de tronco principal até que o recurso esteja completo. Logo, no GitFlow são geradas branches de longa duração. De maneira geral, o GitFlow trabalha com duas branches principais, a Develop e a Master, que duram para sempre; e três branches de suporte, Feature, Release e Hotfix, que são temporários e duram até realizar o merge com as branches principais. Então, ao invés de uma única branch Master, esse fluxo de trabalho utiliza duas branches principais para registrar o histórico do projeto, onde a branch Master armazena o histórico do lançamento oficial, e a branch Develop serve como uma ramificação de integração para recursos. Além disso, é ideal que todos os commits na branch Master sejam marcados com um número de versão. Na imagem abaixo, vemos como é a estrutura do fluxo do GitFlow:

![image.png](https://file.notion.so/f/f/c706f4d2-393c-4c78-84eb-8862c21f2f3f/82c2b17e-e6b3-4597-a602-2ad54533255a/image.png?table=block&id=017b7c7c-c526-490c-b442-ffe94e818a3d&spaceId=c706f4d2-393c-4c78-84eb-8862c21f2f3f&expirationTimestamp=1730505600000&signature=5TicAzquJO_ejTogKvjQwIQNbkXsIeHHEjtE5XXsvQM&downloadName=image.png)

- **Master (ou Main):** é a ramificação principal que contém o código-fonte em produção. Não é permitido realizar alterações (commit) diretamente nessa ramificação. As formas de interagir com essa branch são através de uma Hotfix ou de uma nova Release. Além disso, o último código dessa branch deve sempre estar em produção;
- **Develop:** criada a partir da ramificação Master, ela reúne os códigos de todos os ramos e se comunica com a Master. Ela contém o código-fonte mais atual (sendo então, uma cópia da branch principal), além de todas as novas features estáveis que serão mescladas posteriormente;
- **Feature:** criada a partir da ramificação Develop, é uma branch temporária (portanto, quando finalizada, elas são removidas após realizar o merge com a Branch Develop) que carrega uma nova funcionalidade para o projeto, ela sempre acabará sendo mesclada à própria Develop através de merge. E segue um padrão de nomenclatura “feature/new-feature” (onde “new-feature” se trata do nome do recurso a ser utilizado no fluxo do trabalho). Além disso, por exemplo, se tivermos dez funcionalidades a serem desenvolvidas, criaremos dez branches independentes;
- **Hotfix:** é uma ramificação utilizada para mesclar correções na ramificação principal decorrente de bugs identificados no processo de desenvolvimento. Após a correção do bug, o código irá tanto para a branch master como para a Develop. Essa branch também recebe uma tag indicando a nova versão na Master. A grande diferença entre Feature Branches e Branches de Hotfix é que os Hotfix são criados a partir da Branch Master e quando os finalizamos, eles são mesclados tanto na Branch Master quanto na branch de desenvolvimento. Isso ocorre porque o bug está em ambos os ambientes;
- **Release:** é uma ramificação temporária (branch de lançamento) que fará com que os novos recursos armazenados na Develop sejam mesclados na branch Master (servindo como uma ponte para fazer o merge da Develop para a Master), recebendo uma tag que indica a nova versão do projeto.

## Implementação do GitFlow

Existem duas formas de implementar o GitFlow, a primeira é utilizar os comandos básicos do Git, a outra é utilizar uma CLI (ferramenta que ajuda a gerenciar o fluxo de trabalho do GitFlow com comandos simplificados) que ajuda a simplificar o fluxo do GitFlow. Para instalar a CLI do GitFlow, escolha uma opção de acordo com seu sistema operacional:

- **OSX:** brew install git-flow
- **Linux:** apt install git-flow
- **Windows:** https://git-scm.com/download/win → Já está incluído no Git a partir da versão 2.5.3

## Iniciando o GitFlow

A primeira coisa que temos que fazer é criar uma Branch Develop a partir da Branch Master.

Com comando básico do Git:

```
git checkout -b develop
```

Com a CLI do Git-flow:

```csharp
git flow init
```

A execução deste comando na CLI talvez fará algumas perguntas. Responda tudo afirmativamente e sua Branch Develop será criada.

## Branch Feature

### Criação

Com comandos básicos do Git:

```
git checkout develop
git checkout -b name-feature
```

Com a CLI do Git-flow:

```sql
git flow feature start name-feature
```

### Finalização

Com comandos básicos do Git:

```sql
git checkout develop
git merge name-feature
```

Com a CLI do Git-flow:

```
git flow feature finish name-feature
```

## Branch Hotflix

### Criação

Com comandos básicos do Git:

```
git checkout master
git checkout -b name-hotfix
```

Com a CLI do Git-flow:

```sql
git flow hotfix start name-hotfix
```

### Finalização

Com comandos básicos do Git:

```sql
git checkout master
git merge name-hotfix
git checkout develop
git merge name-hotfix
git tag name-hotfix
```

Com a CLI do Git-flow:

```
git flow hotfix finish name-hotfix
```

Dessa forma, podemos ver o quão útil é a CLI do Git-flow, pois ele simplifica o processo e nos ajuda a não cometer erros.

## Branch Release

### Criação

Com comandos básicos do Git:

```
git checkout develop
git checkout -b release/1.0.0
```

Com a CLI do Git-flow:

```
git flow release start 1.0.0
```

### Finalização

Com comandos básicos do Git:

```
git checkout master
git merge release/1.0.0
git checkout develop
git merge release/1.0.0
git tag 1.0.0
```

Com a CLI do Git-flow:

```
git flow release finish 1.0.0
```

### Fontes de pesquisa

https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow

https://www.alura.com.br/artigos/git-flow-o-que-e-como-quando-utilizar?srsltid=AfmBOoqc5W-tj1GzArRvdtl0OIfCbgPtScBQGveM8UdDLxx_G6O8d8nc

https://www.objective.com.br/insights/git-flow/

https://blog.betrybe.com/git/git-flow/#1
