# **Guia de Contribuição - AcheiUnB**

## **Bem-vindo(a)!**

Obrigado por se interessar em contribuir para o projeto **AcheiUnB**! Este guia foi elaborado para ajudá-lo a colaborar de forma produtiva e consistente com nossa equipe.

---

## **Como contribuir**

1. **Relatar um bug**  
   Se você encontrar um bug, abra uma [issue](https://github.com/unb-mds/2024-2-AcheiUnB/issues) descrevendo o problema:
   - Inclua passos para reproduzir o erro.
   - Anexe logs ou imagens, se necessário.
   - Sugira uma possível solução (opcional).

2. **Sugerir melhorias**  
   Quer melhorar o projeto? Crie uma issue com a tag `enhancement` e descreva:
   - O problema que você quer resolver.
   - Sua ideia ou proposta de solução.
   - Qualquer detalhe adicional que ajude na implementação.

3. **Implementar uma funcionalidade**  
   - Procure uma issue aberta ou crie uma nova descrevendo sua ideia.
   - Discuta sua abordagem antes de começar a codar.
   - Depois de começar a implementação, envie um Pull Request (PR) seguindo os passos detalhados abaixo.

---

## **Regras para Contribuições**

### **1. Branches**
- Use a branch `main` apenas para código testado e funcional.
- Crie uma branch específica para cada contribuição. Nomeie sua branch seguindo o padrão:
  ```
  tipo/nome-da-contribuicao
  ```
  Exemplos:
  - `feat/login-microsoft`
  - `fix/ajuste-autenticacao`
  - `docs/atualizacao-readme`

### **2. Commits**
- Utilize mensagens claras e concisas para os commits.
- Siga o padrão **Conventional Commits**:
  ```
  <tipo>(escopo): mensagem
  ```
  Exemplos:
  - `feat(auth): implementar autenticação Microsoft`
  - `fix(api): corrigir erro no endpoint de listagem`
  - `docs(readme): atualizar instruções de execução`

### **3. Pull Requests**
- Garanta que seu código está atualizado com a branch `main` antes de enviar o PR.
- Siga este modelo de descrição de PR:

  ```
  ## Descrição do Pull Request
  <!-- Descreva de forma clara e objetiva o que foi feito. -->

  ## O que foi feito?
  - [ ] Implementação de ...
  - [ ] Correção de ...

  ## Checklist
  - [ ] Meu código segue as diretrizes do projeto.
  - [ ] Testei minha funcionalidade e ela está funcionando conforme esperado.
  - [ ] Atualizei a documentação, se necessário.
  ```

- Aguarde a revisão de pelo menos um membro da equipe antes de fazer merge.

---

## **Boas Práticas**

### **Código**
- Mantenha o código simples e legível.
- Siga o estilo definido pela equipe para Python (PEP8) e Django.
- Use boas práticas em Docker e controle de dependências.

### **Documentação**
- Atualize a documentação sempre que sua contribuição afetar as instruções de uso.
- Mantenha a clareza no README e outros arquivos de documentação.

### **Testes**
- Sempre adicione testes para novas funcionalidades.
- Garanta que todos os testes existentes estão passando:
  ```bash
  make test
  ```

---

## **Padrões da Comunidade**

### **Código de Conduta**
Este projeto segue o [Código de Conduta do Contributor Covenant](https://github.com/unb-mds/2024-2-AcheiUnB/blob/main/docs/CODE_OF_CONDUCT.md). Seja respeitoso, inclusivo e ajude a manter um ambiente saudável para todos.

### **Colaboração**
- Respeite o trabalho dos outros contribuidores.
- Antes de sugerir mudanças, discuta com a equipe no espaço de issues ou PRs.
- Seja claro em suas comunicações e esteja aberto a feedback.

---

## **Ferramentas e Tecnologias**

- **Backend**: Python (Django, Django Rest Framework)
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker
- **Frontend**: Vue js
- **Testes**: Pytest ou ferramentas nativas do Django

---

## **Contato**

Se tiver dúvidas ou precisar de ajuda, entre em contato conosco pelo e-mail oficial do projeto:
- [acheiunb2024@gmail.com](mailto:acheiunb2024@gmail.com)
