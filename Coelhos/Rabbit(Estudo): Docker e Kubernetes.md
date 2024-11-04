# Docker

## Introdução
Inicialmente, podemos definir Docker como uma plataforma de código aberto (software que permite que qualquer pessoa inspecione, modifique e melhore o seu código-fonte) que, além de facilitar o deploy de uma aplicação, é usado para implantar aplicativos dentro de containers virtuais, permitindo aos desenvolvedores construir, implementar, executar, atualizar e gerenciar esse containers, além de empacotarem suas aplicações em ambientes portáveis e autossuficientes que podem ser executados em qualquer lugar, independentemente do sistema operacional e da infraestrutura de hospedagem.

Contêineres são componentes executáveis padronizados que combinam o código fonte da aplicação com as bibliotecas e dependências do sistema operacional (SO) necessárias para executar esse código em qualquer ambiente (é o Docker Engine que coordena entre o sistema operacional e os contêineres do Docker).

Essa tecnologia de conteinerização cria e usa containers Linux, onde com ele é possível lidar com os containers como se fossem máquinas virtuais modulares e extremamente leves. Além disso, os containers oferecem maior flexibilidade para você criar, implantar, copiar e migrar um container de um ambiente para outro, otimizando, dessa forma, as aplicações na nuvem.

## Como funciona?
É possível dizer que o Docker desempenha um papel crucial no desenvolvimento moderno de software, especificamente na arquitetura de microsserviços, os quais proporcionam uma framework arquitetônica nativa da nuvem. Essa framework compõe uma única aplicação a partir de muitos componentes ou serviços menores, fracamente acoplados e implementáveis de forma independente. Cada serviço pode ser conteinerizado usando o Docker, simplificando a implementação e permitindo que as equipes implantem novas versões e dimensionem as aplicações conforme a necessidade.

A tecnologia Docker usa o kernel do Linux e funcionalidades do kernel, como cGroups e namespaces, para segregar processos, onde assim, eles podem ser executados de maneira independente.

As ferramentas de container, incluindo o Docker, incluem um modelo de implantação com base em imagem. Isso facilita o compartilhamento de uma aplicação ou conjunto de serviços, incluindo todas as dependências deles em vários ambientes. Além disso, o Docker também automatiza a implantação da aplicação (ou de conjuntos de processos que constituem uma app) dentro desse ambiente de containers.

Essas ferramentas baseadas nos containers Linux fazem com que o Docker seja exclusivo e fácil de usar. Elas também oferecem aos usuários acesso sem precedentes a apps e total controle sobre as versões e distribuição, além da habilidade de implantar com rapidez.

Além disso, embora isso possa causar confusão, o Docker não é o mesmo que um container Linux tradicional. A tecnologia Docker foi desenvolvida inicialmente com base na tecnologia LXC, que a maioria das pessoas associa aos containers Linux "tradicionais". No entanto, desde então, essa tecnologia tornou-se independente. O LXC era útil como uma virtualização lightweight, mas não oferecia uma boa experiência para usuários e desenvolvedores. A tecnologia Docker oferece mais do que a habilidade de executar containers: ela também facilita o processo de criação e construção de containers, o envio e o controle de versão de imagens, entre outros.

Enquanto os containers Linux tradicionais usam um sistema init capaz de gerenciar vários processos (isso significa que aplicações inteiras são executadas como uma), a tecnologia Docker, como já dito, incentiva a segregação de aplicações em processos separados e oferece as ferramentas para fazer isso.

A arquitetura do Docker consiste em quatro componentes principais junto com os containers do Docker:
- Cliente Docker: o principal componente para criar, gerenciar e executar aplicativos em container. O cliente Docker é o principal método de controle do servidor Docker por meio de uma ILC, como Prompt de Comando (Windows) ou Terminal (macOS, Linux);
- Servidor Docker: também conhecido como o daemon do Docker. Ele aguarda as solicitações da API REST feitas pelo cliente Docker e gerencia imagens e containers;
- Imagens do Docker: instrua o servidor Docker com os requisitos sobre como criar um container Docker. As imagens podem ser baixadas de sites como Docker Hub. A criação de uma imagem personalizada também é possível — para isso, os usuários precisam criar um Dockerfile e passá-lo para o servidor. Vale a pena notar que o Docker não limpa nenhuma imagem não utilizada, então os usuários precisam excluir dados de imagem eles mesmos, antes que acabe com muitas delas;
- Registro do Docker: um aplicativo do lado do servidor de código aberto usado para hospedar e distribuir imagens do Docker. O registro é extremamente útil para armazenar imagens localmente e manter controle total sobre elas. Como alternativa, os usuários podem acessar o Docker Hub mencionado acima – o maior repositório mundial de imagens do Docker.

## Instalação e funcionalidades
- Instalação do Docker

Para começar a usar o Docker, você precisa instalá-lo em seu sistema. A instalação é simples e pode ser realizada em várias plataformas. O Docker está disponível para Windows, Linux e MacOS.

Para instalar o Docker no Ubuntu, você pode seguir os seguintes passos:

Abra o terminal e atualize o pacote do sistema:
```
$ sudo apt-get update
```
Instale o Docker:
```
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Verifique a instalação do Docker:
```
$ sudo docker run hello-world
```
- Baixando imagens do Docker

Depois de instalar o Docker, você pode baixar imagens de aplicativos pré-configurados do Docker Hub. O Docker Hub é um registro centralizado para imagens Docker e permite que você encontre, baixe e use imagens criadas por outras pessoas.

Para baixar uma imagem do Docker, basta executar o seguinte comando:
```
$ sudo docker pull nome_da_imagem
```
Por exemplo, para baixar a imagem do Ubuntu, você pode usar o seguinte comando:
```
$ sudo docker pull ubuntu
```
- Inicializando um container

Um container é uma instância em execução de uma imagem Docker. Você pode inicializar um container usando o comando docker run. O comando docker run cria e inicia um novo container com base na imagem fornecida.

Para iniciar um container a partir de uma imagem, execute o seguinte comando:
```
$ sudo docker run nome_da_imagem
```
Por exemplo, para iniciar um container a partir da imagem do Ubuntu, você pode usar o seguinte comando:
```
$ sudo docker run -it ubuntu bash
```
- Criando um banco de dados

Docker também pode ser usado para criar bancos de dados. Para criar um banco de dados, você precisa baixar uma imagem de banco de dados e, em seguida, inicializar um container a partir da imagem.

Para criar um banco de dados MySQL, por exemplo, você pode usar o seguinte comando:
```
$ sudo docker run --name nome_container -e MYSQL_ROOT_PASSWORD=senha -d mysql:tag
```
Este comando cria um novo container com o nome "nome_container", define a senha para o usuário root como "senha" e inicia o MySQL como um serviço em segundo plano.
- Criando volumes

Um volume é uma maneira de persistir os dados em um container. Quando um container é destruído, todos os dados armazenados nele são perdidos. No entanto, se você criar um volume, os dados serão armazenados em um local persistente fora do container.
Para criar um volume, execute o seguinte comando:
```
$ sudo docker volume create nome_volume
```
Por exemplo, para criar um volume chamado "dados", você pode usar o seguinte comando:
```
$ sudo docker volume create dados
```
Você também pode criar um volume ao iniciar um container. Para fazer isso, basta adicionar a opção "-v" ao comando "docker run". Por exemplo:
```
$ sudo docker run -v nome_volume:/caminho/no/container nome_da_imagem
```

## Vantagens
O processo de conteinerização, facilitado pelo Docker, permite que vários aplicativos funcionem em diferentes ambientes complexos (exemplo: o Docker permite executar o WordPress em sistemas Windows, Linux e macOS, sem problemas). Dessa forma, ele torna a criação, implantação e gerenciamento de aplicativos muito mais simples e eficiente.

Com isso, podemos dizer que, como os containers são independentes, as equipes podem trabalhar de forma autônoma, liberando novas versões de forma ágil e dimensionando cada serviço conforme necessário, tudo isso com a segurança de que o código funcionará da mesma forma em qualquer ambiente.

Além disso, por exemplo, o Docker também pode ser usado para criar bancos de dados. Nesse caso, você precisa baixar uma imagem de banco de dados e, em seguida, inicializar um container a partir da imagem.

# Kubernetes

## Introdução
Por si só, o Docker consegue gerenciar containers únicos. Conforme você começa a usar cada vez mais containers e apps em containers, segregados em centenas de partes, pode ser difícil gerenciá-los e orquestrá-los. Eventualmente, será necessário parar um pouco e agrupar os containers para oferecer serviços como rede, segurança, telemetria, entre outros, em todos eles. É aí que o Kubernetes entra em cena.

Semelhante ao Docker, o Kubernetes também é uma tecnologia de conteinerização, entretanto, ele se caracteriza como um sistema de orquestração de containers, distribuídos em clusters (agrupamentos de containers que compartilham os mesmos recursos computacionais, como armazenamento), de código aberto.

Dessa forma, podemos dizer que o Kubernetes é uma plataforma open source e uma tecnologia para containers que otimiza a gestão de espaço de dados, além de otimizar a velocidade de processos, sendo fundamental para empresas que executam aplicativos na nuvem.

## Qual sua utiliade?
A função do Kubernetes é ajudar no controle e na gestão dos containers, pois, ao criá-los, eles podem se multiplicar em uma velocidade absurda. Então, para quem deseja criar um site e mantê-lo com uma rápida velocidade de carregamento das páginas, mesmo oferecendo microsserviços, o Kubernetes contribuirá para esse processo.

Além disso, tem-se o objetivo de cuidar do ciclo de vida dos containers dentro do cluster, distribuindo-os conforme suas especificações ou as demandas da sua operação.

Com o Kubernetes, é possível criar aplicativos em ambientes virtuais, sejam em locais híbridos e também em nuvens públicas e privadas. É possível dimensionar o tamanho do cluster para executar determinados serviços, além de otimizar a velocidade para o desenvolvimento.

Sendo assim, é fácil observar a importância da ferramenta por vários motivos como:
- software de código aberto: as ferramentas open source são importantes não apenas pelo fato de estarem disponíveis para quem desejar usá-las, como também por permitirem a adaptação para as necessidades que surgirem;
- atualizações: por ser amplamente usado (e ser código aberto), o Kubernetes ganha implementações e atualizações constantemente, permitindo o acompanhamento de novidades;
- adaptação para qualquer tipo de nuvem: pública, privada ou híbrida, a ferramenta é executável em uma dessas ou mesmo em várias nuvens.

## Implementação e funcionalidades
Na prática, a implementação do Kubernetes exige alguns passos. Primeiro, é preciso criar um cluster de Kubernetes. Com o cluster, será possível o plano de gerenciamento — Control Plane — e a criação dos nós onde são processados os aplicativos. Em seguida, é preciso implantar o primeiro aplicativo: o kubectl. Esse aplicativo será responsável pela interação entre o Kubernetes e o cluster.

Em seguida, é possível explorar o aplicativo, localizando os Pods e os Nodes (nós). Enquanto o Pod agrupa os containers de aplicativos em um local específico, os nós são as máquinas de processamento, podendo ter um ou mais pods.

Para expor o aplicativo publicamente:
- ClusterIP — o serviço fica exposto dentro do cluster, apenas a partir de um endereço de IP;
- NodePort — o serviço fica exposto na mesma porta, no nó selecionado no cluster;
- <NodeIP>:<NodePort> — o serviço fica exposto externamente ao cluster;
- ExternalName — o serviço fica exposto, mas usando um nome arbitrário.

Além disso, a ferramenta possui diversos comandos que garantem mais facilidade no gerenciamento das cargas de trabalho, de forma automatizada e escalável, como:

- kube-apiserver: front end para o gerenciamento de Kubernetes que permite o escalonamento horizontal de instâncias com balanceamento de carga;
- etcd: repositório de apoio do cluster de container que utiliza armazenamento do tipo chave-valor, garantindo consistência e alta disponibilidade;
- kube-scheduler: automação do gerenciamento de componentes das aplicações que atribui um conjunto de servidores de processamento para aplicações que foram criadas sem um nó;
- kube-controller-manager: controlador automatizado, que cuida de diversos aspectos do cluster de containers, como a identificação de indisponibilidades e garantia da execução de processos.

## Vantagens
O Kubernetes apresenta diversas vantagens. Ele oferece maior velocidade no desenvolvimento, permitindo implantar mais de uma vez por dia em vez de fazê-lo mensalmente, caso isso seja preciso. Além disso, existem outros motivos para optar pela utilização da mesma, como:

- orquestração: o armazenamento pode ser desenvolvido e indicado por você. É possível escolher armazenamentos locais e contar com estratégias multi cloudy;
- otimização dos recursos: os clusters de nós podem ser utilizados para executar tarefas nos containers. Dessa forma, você distribui a memória conforme a necessidade;
- autocorreção: em caso de falha de algum container, a ferramenta reinicia o mesmo e, em caso de erro, substitui por outro;
- automatização: o Kubernetes pode ser programado para a criação de containers automaticamente na implantação. Além disso, é possível eliminar containers ou concentrar todos os recursos no novo container;
- segurança da informação: as informações sigilosas podem ser armazenadas e gerenciadas. Com o Kubernetes você pode usar senhas, tokens e chaves, aumentando a segurança e mantendo determinado container em segredo.

## Docker x Kubernetes
Os sistemas não podem ser comparados diretamente, pois o Docker é responsável pela criação de containers e o Kubernetes os gerencia em grande escala. No entanto, o Docker oferece seu próprio sistema de orquestração chamado Docker Swarm. Segue uma tabela com uma comparação do Kubernetes e do Docker Swarm:

![image](https://github.com/user-attachments/assets/36a60e2a-46ed-44a1-9f2d-e47645a25e4d)
- O Kubernetes pode ser usado com ou sem o Docker;
- O Docker não é uma alternativa ao Kubernetes. Portanto, não é uma questão de “Kubernetes vs. Docker”. Trata-se de usar o Kubernetes com o Docker para armazenar seus aplicativos em contêineres e executá-los em escala;
- A diferença entre o Docker e o Kubernetes está relacionada ao papel que cada um desempenha na conteinerização e na execução de seus aplicativos;
- O Docker é um padrão aberto do setor para empacotar e distribuir aplicativos em contêineres;
- O Kubernetes usa o Docker para implantar, gerenciar e escalonar aplicativos conteinerizados.

## Fontes de Pesquisa
https://www.ibm.com/br-pt/topics/docker
https://www.redhat.com/pt-br/topics/containers/what-is-docker
https://www.hostinger.com.br/tutoriais/o-que-e-docker
https://www.dio.me/articles/docker-como-instala-lo-baixar-imagens-inicializar-conteineres-criar-banco-de-dados-e-volumes
https://rockcontent.com/br/blog/kubernetes/
https://cloud.google.com/learn/what-is-kubernetes?hl=pt-BR
https://binario.cloud/blog/o-que-e-cluster-de-container-saiba-a-diferenca-entre-docker-e-kubernetes/#:~:text=Um%20cluster%20de%20container%20%C3%A9%20um%20agrupamento%20de%20cont%C3%AAineres%20que,e%20sem%20concorr%C3%AAncia%20de%20recursos
