# Heroku

### O que é Heroku e como ele pode ajudar no meu projeto?

O Heroku é uma plataforma de computação em nuvem que permite criar, implantar e gerenciar aplicativos de forma simplificada. Fundada em 2007, ela inicialmente suportava apenas a linguagem Ruby, mas atualmente é compatível com diversas linguagens, como Node.js, Java, Python, PHP, Go, Scala e Clojure.

**Como o Heroku pode beneficiar seu projeto:**

1. **Implantação simplificada**: você pode hospedar seu aplicativo na nuvem sem se preocupar com configuração e manutenção de servidores físicos, permitindo maior foco no desenvolvimento do código.
2. **Escalabilidade**: ajusta os recursos do aplicativo conforme a demanda aumenta.
3. **Integração com ferramentas populares**: permite automatizar deploys através de serviços como GitHub.
4. **Suporte a múltiplas linguagens**: atende diversos tipos de aplicações.
5. **Add-ons e extensões**: oferece ferramentas como bancos de dados, monitoramento e cache.

Com o Heroku, você pode tanto hospedar o backend do seu projeto **AcheiUnB**, quanto configurar e gerenciar um banco de dados PostgreSQL, caso necessário.

---

### O Heroku funciona como banco de dados?

O Heroku **não é um banco de dados**, mas oferece o serviço **Heroku Postgres**, que hospeda um banco de dados PostgreSQL gerenciado. Esse serviço é acessível remotamente e cuida de tarefas como backups automáticos, escalabilidade, atualizações e monitoramento.

**Como usar o Heroku Postgres em um projeto Django:**

1. Adicione o Heroku Postgres como um add-on no painel do Heroku.
2. Configure o arquivo `settings.py` do Django para usar a URL de conexão fornecida pelo Heroku:
    
    ```python
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }
    
    ```
    
3. Realize migrações para criar as tabelas no banco:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    
    ```
    

Com isso, o banco de dados será hospedado na nuvem, evitando perdas de dados mesmo em reinicializações do servidor.

---

### O Heroku vai apenas hospedar o banco de dados Postgre?

Sim, o Heroku pode ser usado apenas para hospedar o banco de dados PostgreSQL, por meio do Heroku Postgres. Nesse caso, você pode conectar aplicações que estão hospedadas em outros servidores ao banco gerenciado no Heroku, utilizando a URL de conexão que ele fornece.

Benefícios de usar o Heroku Postgres:

- Configuração fácil e pronta para uso.
- Gerenciamento automático de backups e atualizações.
- Escalabilidade conforme as necessidades do projeto.
- Alta disponibilidade e segurança integrada.

---

### O serviço de hospedagem do Heroku é pago?

O Heroku oferece tanto serviços gratuitos quanto pagos, dependendo das necessidades do projeto.

**Camada Gratuita:**

- Ideal para projetos pequenos, MVPs ou testes.
- Limitações: o aplicativo pode entrar em estado de "dormência" após inatividade.

**Planos Pagos:**

1. **Hobby** (a partir de US$7/mês): para pequenos projetos com mais consistência.
2. **Standard** (a partir de US$25/mês): recomendado para aplicações de negócios.
3. **Performance** (a partir de US$250/mês): para grandes projetos com alta performance.
4. **Enterprise**: preços personalizados para grandes organizações.

Além disso, o Heroku oferece serviços adicionais, como bancos de dados gerenciados (Heroku Postgres), cache em memória (Heroku Redis) e vários add-ons para ampliar funcionalidades.

---

**Conclusão:**
O Heroku é uma excelente opção para hospedar seu projeto Django, seja para gerenciar a aplicação, o banco de dados ou ambos. A camada gratuita é útil para testes e protótipos, enquanto os planos pagos são recomendados para produção e maior escalabilidade.

**Alternativas para o Heroku:**

---

### **1. Render**

**Descrição**: O Render é uma plataforma em nuvem moderna que se tornou uma das alternativas mais populares ao Heroku. Ele oferece serviços de hospedagem para aplicativos web, APIs, bancos de dados e outros serviços.

- **Vantagens**:
    - Oferece um plano gratuito com até 750 horas de uso por mês.
    - Configuração simples e semelhante ao Heroku.
    - Inclui suporte nativo para bancos de dados, como PostgreSQL.
    - Certificados SSL gratuitos e fácil integração com GitHub/GitLab.
- **Limitações** (plano gratuito):
    - Adormecimento de aplicações após inatividade (similar ao Heroku).
- **Ideal para**: Pequenos projetos e MVPs.

[Site oficial: render.com](https://render.com/)

---

### **2. Fly.io**

**Descrição**: Fly.io permite que você execute aplicativos no **edge computing** (ou seja, mais perto dos usuários finais), o que melhora a latência.

- **Vantagens**:
    - Plano gratuito inclui 3 máquinas virtuais com 256 MB de RAM.
    - Facilidade de uso para desenvolvedores que desejam implantar containers Docker.
    - Possui suporte para múltiplas regiões (escolha onde seu aplicativo será hospedado).
- **Limitações**:
    - Sem suporte nativo para bancos de dados no plano gratuito, mas você pode usar serviços externos como o Supabase ou Neon (ver abaixo).
- **Ideal para**: Aplicações baseadas em Docker ou que necessitam de baixa latência.

[Site oficial: fly.io](https://fly.io/)

---

### **3. Railway**

**Descrição**: Railway é uma plataforma em nuvem com uma experiência de usuário muito simplificada, focada em ser fácil para desenvolvedores.

- **Vantagens**:
    - Plano gratuito com $5 de crédito mensal (aproximadamente 500 horas).
    - Configuração simples e integração com GitHub.
    - Suporte nativo para bancos de dados PostgreSQL e MySQL.
    - Aplicações não entram em estado de dormência.
- **Limitações**:
    - Créditos gratuitos limitados (após isso, requer pagamento).
- **Ideal para**: Projetos que precisam de uma experiência simples e sem muita configuração.

[Site oficial: railway.app](https://railway.app/)

---

### **4. Vercel**

**Descrição**: O Vercel é uma plataforma focada em aplicações **frontend**, mas também suporta APIs via serverless functions (funções sem servidor).

- **Vantagens**:
    - Plano gratuito sem limite de tempo.
    - Muito eficiente para projetos baseados em frameworks frontend como Next.js.
    - Deploy super rápido e fácil de configurar.
- **Limitações**:
    - Não é ideal para backend complexo, pois foca em funções serverless.
- **Ideal para**: Aplicações frontend ou projetos com backend simples.

[Site oficial: vercel.com](https://vercel.com/)

---

### **5. Netlify**

**Descrição**: Assim como o Vercel, o Netlify é focado em aplicações frontend, mas também suporta funções serverless para criar APIs.

- **Vantagens**:
    - Plano gratuito robusto.
    - Facilidade de integração com GitHub.
    - Hospedagem estática rápida e gratuita.
- **Limitações**:
    - Suporte limitado para backend completo.
- **Ideal para**: Aplicações frontend ou SPAs (Single Page Applications).

[Site oficial: netlify.com](https://www.netlify.com/)

---

### **6. Supabase**

**Descrição**: O Supabase é uma alternativa de código aberto ao Firebase, que fornece backend como serviço. Ele inclui banco de dados PostgreSQL, autenticação, armazenamento e APIs automáticas.

- **Vantagens**:
    - Plano gratuito robusto com banco de dados PostgreSQL gerenciado.
    - Fácil integração com aplicações Django ou qualquer aplicação que use PostgreSQL.
    - Open source, permitindo maior flexibilidade.
- **Limitações**:
    - Recursos gratuitos limitados para projetos maiores.
- **Ideal para**: Projetos que necessitam de backend completo e gerenciamento de banco de dados.

[Site oficial: supabase.com](https://supabase.com/)

---

### **7. AWS Free Tier**

**Descrição**: A Amazon Web Services (AWS) oferece um nível gratuito para muitos de seus serviços, incluindo EC2 (máquinas virtuais), RDS (banco de dados relacional) e Lambda (funções serverless).

- **Vantagens**:
    - Muito poderoso e flexível.
    - Recursos gratuitos disponíveis por 12 meses (limite de uso, como 750 horas de instância EC2/mês).
- **Limitações**:
    - Curva de aprendizado mais íngreme.
    - Configuração manual, exigindo maior conhecimento técnico.
- **Ideal para**: Projetos que exigem maior controle sobre a infraestrutura.

[Site oficial: aws.amazon.com](https://aws.amazon.com/)

---

### **Qual escolher para o seu projeto AcheiUnB?**

Se você está buscando algo prático e gratuito, considere estas opções:

- **Railway**: Fácil de usar, suporta backend completo e bancos de dados.
- **Render**: Muito parecido com o Heroku, com maior flexibilidade.
- **Supabase**: Excelente para backend com banco de dados PostgreSQL.

Caso deseje explorar alternativas mais completas, o **AWS Free Tier** pode ser interessante, mas exige mais conhecimento técnico.
