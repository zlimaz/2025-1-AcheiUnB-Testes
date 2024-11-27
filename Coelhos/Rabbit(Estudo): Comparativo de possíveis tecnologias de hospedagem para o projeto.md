# _Heroku x Render x AWS_
> Considerando as versões gratuitas!
## Heroku
De acordo com o próprio **Heroku**: _If you are registered with the GitHub Student Developer Pack, you are eligible to receive
platform credits worth $13 per month for 24 months (for a total value of $312)._
- Planos normais:

![image](https://github.com/user-attachments/assets/9e4f94ff-c45f-4b63-ad87-90da196377a5)

Considerando o crédito máximo de $13 por mês, o único plano possível seria o _Eco_, o qual possui a seguinte descrição:

![image](https://github.com/user-attachments/assets/0fd7d991-3786-4806-9afa-288ffc703135)

- Vantagens do Heroku Eco:
> Custo Acessível: O plano Eco é uma opção econômica, ideal para projetos pessoais, protótipos ou aplicações de pequeno porte que não
exigem recursos robustos;
>
> Facilidade de Uso: O Heroku é conhecido por sua interface intuitiva e simplicidade no processo de deploy, permitindo que desenvolvedores
concentrem-se no código sem se preocupar com a infraestrutura subjacente;
>
> Escalabilidade Simples: Embora limitado, o plano Eco permite escalonamento básico, facilitando o aumento de recursos conforme a demanda
da aplicação cresce;
>
> Integração com Add-ons: Mesmo no plano Eco, é possível integrar diversos add-ons disponíveis no Heroku, como bancos de dados e
ferramentas de monitoramento, ampliando as funcionalidades da aplicação.
- Desvantagens do Heroku Eco:
> Recursos Limitados: O plano Eco oferece recursos computacionais restritos, o que pode não ser suficiente para aplicações com tráfego
elevado ou que demandam alto desempenho;
>
> Hibernação de Dynos: Aplicações no plano Eco podem entrar em modo de hibernação após um período de inatividade, resultando em tempos
de resposta mais lentos no primeiro acesso após a hibernação;
>
> Suporte Limitado: O suporte técnico no plano Eco é básico, podendo não atender adequadamente a necessidades mais complexas ou urgentes;
>
> Menor Prioridade de Recursos: Aplicações no plano Eco podem ter menor prioridade em relação a recursos de processamento e rede, afetando
o desempenho em momentos de alta demanda.
- Quando usar o Heroku?
> Se o objetivo principal é prototipar ou testar rapidamente;
>
> Para equipes com menos experiência em configuração de servidores.

## AWS
- Informações sobre a tier gratuita do **AWS**:

![image](https://github.com/user-attachments/assets/826883a1-b322-4fea-8e6a-6af50f8e6777)
- Vantagens do AWS:
> Alta escalabilidade: Ideal para projetos com potencial de crescimento;
>
> Amplo ecossistema: Serviços como EC2, RDS (para PostgreSQL), S3 (armazenamento de arquivos) e CloudFront (CDN);
>
> Controle total: Você pode personalizar o ambiente como desejar.
- Desvantagens do AWS:
> Complexidade: Requer mais conhecimento técnico para configurar e gerenciar;
> 
> Custo variável: Apesar do plano gratuito, o custo pode aumentar rapidamente ao ultrapassar os limites;
> 
> Curva de aprendizado: A interface da AWS não é tão intuitiva para iniciantes.
- Quando usar o AWS?
> Se o objetivo principal é criar um sistema altamente escalável e configurável, planejando o futuro do projeto;
> 
> Se a equipe tem alguém com experiência em AWS ou tempo para aprender.

O Amazon Web Service (AWS) nos traz Elastic Beanstalk (serviço que permite implementar e gerenciar aplicações na nuvem sem precisar
configurar diretamente a infraestrutura subjacente, como servidores, redes e balanceadores de carga).

O AWS também é seguro (você pode configurar o nível de segurança conforme achar necessário), fácil de alterar, flexibilidade, entre outros,
possuindo, no geral, custo baixo e opção gratuita, porém é preciso cadastrar o seu cartão de crédito (mesmo sendo grátis).

## Render
Sobre _"Monthly usage limits - Free instance hours"_, de acordo com o próprio **Render**, _Render grants 750 Free instance hours to each
workspace per calendar month_, onde:
- _A Free web service consumes these hours as long as it’s running (spun-down services don’t consume Free instance hours)._
- _If you consume all of your Free instance hours during a given month, Render suspends all of your Free web services until the start
of the next month._
- _At the start of each month, your Free instance hours reset to 750 (remaining hours don’t roll over)._

![image](https://github.com/user-attachments/assets/0a6219f4-8db4-4142-b03f-3512f3f9e5bf)

- Vantagens do Render:
> Fácil de configurar: Similar ao Heroku em simplicidade, com menos limitações;
>
> Custo baixo: O plano gratuito inclui 750 horas/mês, suficiente para uma aplicação em estágio inicial;
>
> Pronto para produção: Não há hibernação, e o serviço é mais estável para uso real;
>
> Integração: Suporte nativo para PostgreSQL e configuração simplificada para deploys automáticos.
- Desvantagens do Render:
> Menos recursos avançados: Comparado à AWS, é menos flexível e personalizável;
>
> Desempenho: Não é tão robusto quanto um serviço como AWS para demandas muito altas.
- Quando usar o Render?
> Se o objetivo principal é hospedar uma aplicação pronta para produção com custo baixo e simplicidade.

O Render é uma plataforma que inclui hospedagem de banco de dados, CRONs (tarefas que você configura para serem executadas de forma
periódica), entre outros, onde as aplicações ficam inativas após 15 minutos sem nenhuma requisição e voltam assim que é realizada uma
nova requisição, porém, tem-se a possibilidade de [usar a versão free do render sem downtime](https://www.tabnews.com.br/nathsouza/dica-usar-a-versao-free-do-render-sem-downtime).

É importante ressaltar sua simplicidade, aporte para diversas ferramentas, opção de migrar os deploys do Heroku, além de outros benefícios.

## Ideias finais
Considerando que o **AcheiUnB** está em desenvolvimento e visa ser uma plataforma útil para estudantes da UnB, a análise seria:
- Curto Prazo (Desenvolvimento e Testes):
  - Render (Grátis ou Barato): É mais estável que o Heroku (sem hibernação) e fácil de usar, sendo adequado para o estágio inicial do
  projeto.
  - Heroku (Eco): Se o foco for simplicidade e a equipe não se incomodar com a hibernação.
- Longo Prazo (Produção):
  - AWS: Quando o sistema crescer e precisar de escalabilidade (medida de flexibilidade para lidar com grandes volumes de usuários) e
  robustez, a AWS será uma solução poderosa. Porém, requer mais tempo para configurar e gerenciar, podendo ser mais desafiador, mas
  sendo um aprendizado valioso.
## Fonte de pesquisa
> [Heroku para estudantes](https://www.heroku.com/github-students)
>
> [Heroku](https://www.heroku.com/pricing)
> 
> [AWS](https://aws.amazon.com/pt/free/?trk=0b854ede-d445-4eda-b7c7-2a23a18bf271&sc_channel=ps&ef_id=Cj0KCQiAgJa6BhCOARIsAMiL7V9b56Z9lBR9vFg8MPdnmMTw5JAmUFJSMfh1mwJWmEDmiba5FcFl8bsaAqAhEALw_wcB:G:s&s_kwcid=AL!4422!3!561843094992!e!!g!!amazon%20aws!15278604638!130587772500&gclid=Cj0KCQiAgJa6BhCOARIsAMiL7V9b56Z9lBR9vFg8MPdnmMTw5JAmUFJSMfh1mwJWmEDmiba5FcFl8bsaAqAhEALw_wcB&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
> 
> [Render](https://render.com/docs/free#monthly-usage-limits)
> 
> [Alternativas para o Heroku](https://coodesh.com/blog/candidates/heroku-acabou-e-agora-veja-alternativas/)
