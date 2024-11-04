# Tecnologias front-end </> 🎨

**Frameworks**

Começamos a pesquisa procurando por quais são os frameworks front-end  mais adequados para integrar com o Djando, framework escolhido pelo time de back.

Estas foram as opções:

### 1. React

https://react.dev/learn

- • **Vantagens**: Popular e tem grande suporte da comunidade, excelente para construir interfaces de usuário dinâmicas e interativas. Há muitos pacotes e bibliotecas que complementam React para diferentes necessidades.
- **Curva de aprendizado**: Moderada. É necessário aprender JSX (uma sintaxe similar a HTML no JavaScript) e entender o conceito de estado e componentes funcionais.
- Pré-requisitos: JavaScript ES6+, HTML, CSS, JSX, noções de estado, Node.js, npm
- **Estrutura**: Biblioteca leve e flexível focada no componente visual; depende de bibliotecas adicionais para roteamento, gerenciamento de estado, e requisições HTTP (como React Router, Redux, e Axios).
- **Uso**: Flexível para diversos tipos de projeto, pois é mais uma biblioteca que um framework completo.
- • **Integração com Django**: Django REST Framework é frequentemente usado para expor uma API que o React consome, permitindo uma separação limpa entre o front-end e o back-end. Além disso, bibliotecas como **`django-webpack-loader`** ajudam a servir arquivos React dentro dos templates de Django.

### 2. Vue.js

https://vuejs.org/guide/introduction

- • **Vantagens**: Simples de aprender e configurar, especialmente para projetos que requerem interatividade incremental, pois pode ser adicionado gradualmente a um projeto Django sem reescrever o front-end todo.
- **Curva de aprendizado**: Baixa a moderada. Usa uma sintaxe semelhante a HTML, CSS e JavaScript, o que facilita para iniciantes. É considerado fácil de entender, especialmente para quem conhece HTML.
- Pré-requisitos: JavaScript ES6+, HTML, CSS, conceitos de componente, sintaxe de templates
- **Estrutura**: Framework progressivo. Oferece uma solução completa com seu próprio roteador e biblioteca de gerenciamento de estado (Vue Router e Vuex).
- **Uso**: Bom para projetos de pequeno a médio porte. A arquitetura progressiva permite adicionar complexidade conforme necessário.
- • **Integração com Django**: Similar ao React, Vue pode se comunicar com o back-end Django via uma API RESTful. Também é possível configurar o Webpack com

### 3. Angular

https://v17.angular.io/docs

- • **Vantagens**: Popular e tem grande suporte da comunidade, excelente para construir interfaces de usuário dinâmicas e interativas. Há muitos pacotes e bibliotecas que complementam React para diferentes necessidades.
- • **Integração com Django**: Django REST Framework é frequentemente usado para expor uma API que o React consome, permitindo uma separação limpa entre o front-end e o back-end. Além disso, bibliotecas como **`django-webpack-loader`** ajudam a servir arquivos React dentro dos templates de Django.
- **Curva de aprendizado**: Alta. É necessário entender TypeScript, injeção de dependência e o uso extensivo de decorators. A curva pode ser acentuada devido ao uso de arquiteturas baseadas em módulos e componentes.
- Pré-requisitos: TypeScript, JavaScript ES6+, HTML, CSS, Arquitetura de componentes e módulos
- **Estrutura**: Framework completo e robusto, com tudo embutido (roteamento, validação de formulários, animações, serviços HTTP, etc.), mas rígido em termos de estrutura.
- **Uso**: Recomendado para projetos de médio a grande porte, onde uma estrutura robusta e de longo prazo é necessária

… Alpine.js, Slelte, HTMX … foram opções mais simples

Resumindo: 

| Aspecto | React | Vue | Angular |
| --- | --- | --- | --- |
| **Link da Documentação** | [React Documentation](https://react.dev/learn) | [Vue.js Documentation](https://vuejs.org/guide/introduction) | [Angular Documentation](https://v17.angular.io/docs) |
| **Vantagens** | Popular, grande suporte da comunidade, ideal para interfaces dinâmicas e interativas. Muitos pacotes e bibliotecas disponíveis. | Simples de aprender e configurar, ideal para interatividade incremental. Pode ser adicionado gradualmente a projetos existentes. | Popular, grande suporte da comunidade, excelente para interfaces dinâmicas. Oferece uma solução completa e robusta. |
| **Curva de Aprendizado** | Moderada; necessário aprender JSX e conceitos de estado e componentes funcionais. | Baixa a moderada; usa sintaxe semelhante a HTML, CSS e JavaScript, fácil para iniciantes. | Alta; exige compreensão de TypeScript, injeção de dependência e uso extensivo de decorators. |
| **Pré-requisitos** | JavaScript ES6+, HTML, CSS, JSX, noções de estado, Node.js, npm | JavaScript ES6+, HTML, CSS, conceitos de componente, sintaxe de templates | TypeScript, JavaScript ES6+, HTML, CSS, arquitetura de componentes e módulos |
| **Estrutura** | Biblioteca leve e flexível focada em componentes visuais; depende de bibliotecas adicionais (React Router, Redux, Axios). | Framework progressivo; solução completa com roteador e biblioteca de gerenciamento de estado (Vue Router, Vuex). | Framework completo e robusto; inclui roteamento, validação de formulários, animações, serviços HTTP. |
| **Uso** | Flexível para diversos tipos de projeto; mais uma biblioteca do que um framework completo. | Bom para projetos de pequeno a médio porte; complexidade pode ser adicionada conforme necessário. | Recomendado para projetos de médio a grande porte; estrutura robusta e de longo prazo. |
| **Integração com Django** | Utiliza Django REST Framework para expor APIs consumidas pelo React. `django-webpack-loader` pode servir arquivos React dentro de templates Django. | Semelhante ao React; se comunica com o back-end Django via API RESTful. Possível configuração do Webpack para integração. | Usa Django REST Framework para expor APIs, permitindo uma separação clara entre front-end e back-end. |

**Formatadores de código**

Padronização de código é muito importante para garantir a uniformidade e legibilidade do código conjuto. Aqui vão algumas sugestões:

Para Java Script/Type Script :  https://prettier.io/docs/en/

Para python: https://github.com/psf/black

Ambos possum extensões no VSCode facilmente instáveis


# Figma
https://help.figma.com/hc/pt-br

Na última sprint o figma foi apresentado porém agora irei aprofundar mais nele, que será uma ferramenta utilizada no nosso projeto.

Algumas de suas principais funcionalidades são:
Design de Interfaces: oferece uma variedade de ferramentas para criar layouts, botões, ícones e outros elementos visuais. Os usuários podem desenhar formas, aplicar estilos e criar componentes reutilizáveis.

Prototipagem: é possível conectar diferentes telas e adicionar interações, permitindo que os usuários experimentem a navegação do produto antes mesmo de sua implementação.

Colaboração em Tempo Real: na versão gratuita, até duas pessoas podem trabalhar no mesmo projeto simultaneamente, fazendo comentários, sugerindo alterações e visualizando o progresso em tempo real.

Componentes e Estilos: ele permite a criação de componentes e estilos compartilhados, garantindo consistência em todo o projeto e facilitando atualizações em massa.

Integração com Desenvolvimento: Designers podem gerar códigos CSS e exportar ativos gráficos, facilitando a transição do design para o desenvolvimento. O Figma também suporta plugins que conectam a ferramenta a outras plataformas e fluxos de trabalho.

Entre esses plugins citados existem alguns que facilitam a integração com o Vue.js e o Tailwind CSS.

# Bibliotecas CSS

## Tailwind CSS
https://tailwindcss.com/docs/installation

Tailwind CSS é uma estrutura CSS de código aberto. Ao contrário de outros frameworks, como o Bootstrap, ele não fornece uma série de classes predefinidas para elementos como botões ou tabelas. Ele foi lançado em maio de 2019. 

No seu ano de lançamento entre outras bibliotecas CSS possuia cerca de 6% de uso e uma taxa de satisfação de 81%. Teve um crescimento muito grande e em 2020 pulou pra 26% de popularidade e uma taxa de satisfação de 87%.

Um dos principais conceitos do Tailwind é o “utility-first”, invés de criar classes baseadas em componentes (butões, tabelas, formulários), elas são criadas baseadas em um estilo específico de elemento (cor amarela, fonte negrito, texto largo). Cada uma dessas classes é chamada de Classes Utilitárias. Elas permitem controlar um grande número de propriedades CSS.

Aqui está um exemplo de um código feito com CSS padrão:

```CSS
<div class="chat-notification">
  <div class="chat-notification-logo-wrapper">
    <img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div class="chat-notification-content">
    <h4 class="chat-notification-title">ChitChat</h4>
    <p class="chat-notification-message">You have a new message!</p>
  </div>
</div>

<style>
  .chat-notification {
    display: flex;
    align-items: center;
    max-width: 24rem;
    margin: 0 auto;
    padding: 1.5rem;
    border-radius: 0.5rem;
    background-color: #fff;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  }
  .chat-notification-logo-wrapper {
    flex-shrink: 0;
  }
  .chat-notification-logo {
    height: 3rem;
    width: 3rem;
  }
  .chat-notification-content {
    margin-left: 1.5rem;
  }
  .chat-notification-title {
    color: #1a202c;
    font-size: 1.25rem;
    line-height: 1.25;
  }
  .chat-notification-message {
    color: #718096;
    font-size: 1rem;
    line-height: 1.5;
  }
</style>

```

E o mesmo código feito usando Tailwind:

```CSS

<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center gap-x-4">
  <div class="shrink-0">
    <img class="size-12" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div>
    <div class="text-xl font-medium text-black">ChitChat</div>
    <p class="text-slate-500">You have a new message!</p>
  </div>
</div>

```

Ele funciona escanenado todos os arquivos HTML, componentes JavaScript e qualquer outro template por nomes de classes, gerando o estilo correspondente e escrevendo eles em um arquvio CSS estático.

Como instalar: Em sua documentação existe um guia específico para instalação em diversos frame-work. Caso o Framework desejado não esteja lá existe um tutorial mais genérico.

### Responsividade

Com o Tailwind é mais fácil fazer uma aplicação responsiva, já que todas as classe utilitárias podem ser aplicadas condicionalmente dependendo do tamanho da tela do usuário.

### Modo Noturno

O Tailwind inclui uma variante “dark”, que estiliza o site de forma diferente de acordo com a preferência do sistema operacional. Mas também é possível fazer essa alteração de forma manual.

## Bootstrap
https://getbootstrap.com/docs/5.3/getting-started/introduction/

Diferente do Tailwind, Bootstrap fornece componentes prontos para serem usados. É baseado em estilos pré-definidos.

O Bootstrap também é personalizável, porém de forma mais  rigorosa, já que ele segue um estilo próprio, o “Bootstrap Look”. Para alterar esse estilo é necessário modificar ou sobrescrever o CSS padrão.

## Otimização

- **Bootstrap:** Inclui um conjunto completo de estilos e componentes, então o arquivo CSS pode ser grande, mesmo se não todos os componentes forem usados.
- **Tailwind**: Usa JIT (Just-in-Time Compilation) para gerar apenas as classes realmente usadas no HTML, resultando em um arquivo CSS final muito menor e específico para cada projeto

## Curva de Aprendizado

- **Bootstrap**: Mais fácil para iniciantes e rápido de aprender, pois oferece componentes prontos e não exige um conhecimento profundo de CSS.
- **Tailwind**: Requer um entendimento básico de CSS para aproveitar suas classes utilitárias. A princípio, pode parecer mais complexo, mas oferece grande flexibilidade e controle sobre o design, o que é vantajoso para projetos customizados.

# Vercel
https://vercel.com/docs

Ferramenta usada pela equipe SuaGradeUnb, e que tem como função atuar na etapa de **deploy e hospedagem** de uma aplicação. Seu papel é pegar o código final do projeto e disponibilizá-lo online, otimizando a entrega e escalabilidade do site ou aplicação.

Focada em projetos JavaScript, especialmente aqueles baseados em frameworks como Next.js, Nuxt.js (baseado em Vue.js), React e o próprio Vue.js. A Vercel simplifica o processo de deploy e fornece otimizações automáticas para performance e SEO, além de suporte a SSR (renderização do lado do servidor) e CDN global para distribuir o conteúdo de forma rápida.

# Vite
https://vite.dev/guide/

**Vite** é uma ferramenta de build e desenvolvimento focada em modernizar e otimizar o fluxo de trabalho de projetos front-end. Criado por Evan You, o mesmo criador do Vue.js, Vite tem uma ênfase em desempenho e simplicidade.
Para produção, Vite utiliza o **Rollup** como bundler, otimizando a saída final e garantindo que os arquivos sejam minificados e preparados para um desempenho máximo em ambientes de produção.

Quando falamos que o **Vite** utiliza o **Rollup** como bundler para a construção de aplicações em produção, estamos nos referindo ao processo de empacotar e otimizar os arquivos da aplicação para serem servidos em um ambiente de produção. Vamos entender isso em mais detalhes:

### O que é Bundling?

**Bundling** é o processo de agrupar vários arquivos de código (JavaScript, CSS, imagens, etc.) em um ou mais arquivos menores que podem ser carregados de forma mais eficiente pelo navegador. Isso é importante para melhorar o desempenho de carregamento da página, pois reduz o número de requisições HTTP e melhora o tempo de resposta.

### O Papel do Rollup no Vite

**Rollup** é um bundler moderno e muito eficiente, que se destaca em criar pacotes otimizados, especialmente para bibliotecas e aplicações front-end. Quando você usa Vite para desenvolver sua aplicação, o fluxo de trabalho é o seguinte:

1. **Desenvolvimento**:
    - Durante o desenvolvimento, o Vite não usa o Rollup. Em vez disso, ele utiliza um servidor de desenvolvimento com Hot Module Replacement (HMR) e serve arquivos diretamente do sistema de arquivos. Isso proporciona uma experiência de desenvolvimento mais rápida e eficiente, já que não há necessidade de empacotar toda a aplicação a cada alteração.
2. **Build para Produção**:
    - Quando você está pronto para implantar sua aplicação, você executa o comando de build (`vite build`). Neste momento, o Vite invoca o Rollup para empacotar e otimizar seus arquivos para produção.
    - O Rollup faz várias otimizações durante esse processo, como:
        - **Minificação**: Reduz o tamanho dos arquivos, removendo espaços em branco, comentários e outros elementos desnecessários.
        - **Árvore de eliminação**: Remove código não utilizado, garantindo que apenas o código necessário seja incluído no bundle final.
        - **Divisão de código**: Se a aplicação for grande, o Rollup pode dividir o código em múltiplos pacotes, permitindo que os navegadores carreguem apenas o que é necessário.
3. **Saída Final**:
    - O resultado do processo de build do Rollup é um conjunto de arquivos otimizados que estão prontos para serem servidos em um servidor. Esses arquivos são geralmente colocados em uma pasta chamada `dist` (ou `build`, dependendo da configuração).
    - Os arquivos de saída incluem:
        - **JavaScript**: Um ou mais arquivos JavaScript que contêm o código da aplicação.
        - **CSS**: Arquivos de estilo que foram processados e otimizados.
        - **Outros ativos**: Qualquer imagem ou fonte que a aplicação utilize.
