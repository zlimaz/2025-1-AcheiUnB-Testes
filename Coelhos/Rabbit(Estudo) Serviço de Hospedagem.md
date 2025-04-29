# Serviço de Hospedagem

## O que é?
Hospedagem é o serviço que fornece a infraestrutura necessária para que uma **aplicação web fique acessível para os usuários na internet**.
Isso inclui armazenamento de arquivos, servidores, conexão com a internet e suporte técnico.

## Como funciona?
Basicamente, os arquivos e dados do site ou aplicativo são armazenados e disponibilizados em um servidor (funciona como um aluguel de um
espaço digital para armazenar os arquivos e dados de um site, permitindo que ele fique disponível na internet).

## Tipos de hospedagem + vantagens e desvantagens
- **Hospedagem Compartilhada:** Várias aplicações dividem os recursos de um mesmo servidor;

✅ Vantagens: Custo baixo, ideal para projetos pequenos;

❌ Desvantagens: Limitação de recursos e possíveis problemas de desempenho devido à sobrecarga de outros usuários no servidor.

- **Servidores VPS (Virtual Private Server):** O servidor físico é particionado em várias máquinas virtuais independentes;

✅ Vantagens: Mais controle e recursos dedicados que a hospedagem compartilhada;

❌ Desvantagens: Exige mais conhecimento técnico e custa mais caro.

- **Hospedagem em Nuvem (Cloud Hosting):** A aplicação é hospedada em múltiplos servidores interconectados;

✅ Vantagens: Alta escalabilidade, confiabilidade e cobrança geralmente por uso;

❌ Desvantagens: Complexidade de configuração e custos variáveis.

- **Servidores Dedicados:** Você aluga um servidor inteiro para sua aplicação;

✅ Vantagens: Controle total sobre o ambiente e recursos;

❌ Desvantagens: Alto custo e exige experiência técnica.

- **PaaS (Platform as a Service):** Plataformas que gerenciam infraestrutura e permitem que você foque no desenvolvimento (exemplos:
Heroku, Google App Engine);

✅ Vantagens: Fácil de usar, ideal para desenvolvedores iniciantes;

❌ Desvantagens: Flexibilidade limitada e custo relativamente alto.

- **Servless:** O provedor gerencia a execução do código, escalando automaticamente (exemplo: AWS Lambda).

✅ Vantagens: Paga apenas pelo tempo de execução;

❌ Desvantagens: Adequado apenas para funções pequenas ou aplicações específicas.

## Critérios para a escolha de um serviço de hospedagem
- **Requisitos da aplicação:** Inclui o tipo de tecnologia utilizada (Django, Node.js etc), o banco de dados essencial (PostgreSQL, MySQL etc),
além da necessidade de escalabilidade ou não;
- **Preço:** Avaliar o orçamento (serviços em nuvem podem ser mais caros do que VPS, por exemplo);
- **Desempenho:** Latência e tempos de resposta, e capacidade de lidar com tráfego crescente;
- **Suporte técnico:** Serviços com suporte 24/7 são ideais para evitar problemas críticos, por exemplo;
- **Segurança:** Certificados SSL (proteger conexões com HTTPS), backups, firewalls e proteção contra DDoS;
- **Localização do servidor:** É importante escolher servidores próximos do público-alvo (no caso desse projeto, hospedar em um servidor localizado no Brasil ou na América Latina, por exemplo) para melhorar a latência (atraso que uma mensagem leva de um ponto a outro, sendo medida em ping).

## Principais provedores de hospedagem
O **provedor de hospedagem** é responsável por garantir que o site funcione corretamente, protegê-lo de ataques e transferir o conteúdo
para o navegador do usuário.
- **Amazon Web Services (AWS):** Oferece recursos robustos e flexíveis, sendo ideal para empresas ou projetos que precisam de alta escalabilidade (o serviço cresce para lidar com um aumento na demanda);
- **Google Cloud Platform (GCP):** Focado em big data e inteligência artificial, sendo bom para aplicações que demandam alta disponibilidade;
- **Microsoft Azure:** Integração com ferramentas Microsoft, sendo ideal para quem usa tecnologias Microsoft (e.g., .NET);
- **DigitalOcean:** Focado em simplicidade e desenvolvedores, sendo uma boa opção para pequenas e médias empresas;
- **Heroku:** Simplicidade na implantação de aplicativos, sendo ideal para projetos em fase inicial;
- **HostGator e Bluehost:** Opções tradicionais de hospedagem compartilhada e VPS.

## Ferramentas complementares
- **Docker:** Para criar ambientes consistentes para a aplicação (o Docker Compose facilita o deploy de aplicações em contêineres);
- **CI/CD:** Integração contínua com ferramentas, como GitHub Actions e Jenkins, para automatizar deploys;
- **Gerenciadores de Banco de Dados:** PostgreSQL, MySQL, ou outros.

## Diferenças entre PaaS, IaaS e SaaS
- **PaaS (Plataforma como Serviço)** -> Exemplos: Heroku, Google App Engine:
    - O provedor gerencia infraestrutura, sistema operacional e runtime;
    - Foco no desenvolvimento de aplicações;
    - Ideal para quem quer simplicidade e menos preocupação com infraestrutura.

- **IaaS (Infraestrutura como Serviço)** -> Exemplos: AWS EC2, Google Compute Engine, DigitalOcean:
  - Oferece servidores virtuais e recursos brutos;
  - O usuário gerencia o sistema operacional, middleware e aplicação;
  - Maior controle, mas exige mais trabalho.

- **SaaS (Software como Serviço)** -> Exemplos: Google Workspace, Dropbox:
  - Oferece aplicações prontas para uso;
  - O provedor gerencia tudo, o usuário apenas usa o serviço.

## Diferença entre hospedagem gerenciada e não gerenciada
- **Hospedagem gerenciada:** O provedor cuida de atualizações, backups e segurança, sendo ideal para quem deseja simplicidade e foco no desenvolvimento;
- **Hospedagem não gerenciada:** O usuário gerencia todos os aspectos do servidor, incluindo configuração e segurança, havendo um maior controle, mas exigindo mais conhecimento técnico.
