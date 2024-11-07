## O que são Testes Unitários?

Um teste unitário basicamente é o teste da menor parte testável de um programa.  
Se você programa em uma linguagem que suporte o paradigma funcional, por exemplo, a menor parte testável do seu código deve ser uma função. Então, um teste unitário seria o teste de qualquer função. No caso de orientação a objetos, seria o teste de um método de um objeto.

## Para que servem Testes Unitários?

Perguntar para que servem testes unitários ou qualquer outro teste automatizado é uma ótima pergunta, afinal existem diversas formas que aparentemente são mais rápidas de testar se minha função está fazendo o que deveria. Eu poderia simplesmente executar o código para verificar se está funcionando. Então, por que motivo vou escrever outro código para testar o meu código? O que garante que o segundo código funciona? Quem testa o teste?  
Testes unitários, assim como qualquer teste automatizado, não servem principalmente para verificar se uma função específica está funcionando, mas sim para garantir que sua aplicação continue funcionando após alguma alteração em sua base de código.

## Exemplos de Ferramentas de Testes Unitários

**Python:**
- `unittest` (nativo)
- `pytest`
- `nose2`

**JavaScript/TypeScript:**
- `Jest`
- `Mocha` com `Chai`
- `Jasmine`

**C/C++:**
- `Google Test` (gtest)
- `CppUnit`

## O que é o CodeCov?

CodeCov é uma ferramenta que mede e visualiza a cobertura de código nos testes, integrando-se a repositórios como GitHub e GitLab. Ela fornece relatórios detalhados sobre quais partes do código foram testadas, destacando áreas que precisam de mais cobertura.

## O que é Cobertura de Código?

Cobertura de código, ou *code coverage*, é uma métrica usada em desenvolvimento de software para medir a quantidade de código que é executada durante os testes. Ela indica quais partes do código foram verificadas, ajudando a identificar áreas não testadas e garantindo que a maioria das funcionalidades seja validada.

A prática de testar o código antes de colocá-lo em produção é essencial e traz benefícios como:

- **Garante qualidade**: ajuda a identificar áreas do código que não foram testadas.
- **Reduz riscos**: diminui a chance de bugs ou comportamentos inesperados em produção.
- **Aumenta a confiança**: maior cobertura indica que o sistema foi amplamente testado.
- **Facilita a manutenção**: contribui para uma base de código mais robusta e menos propensa a erros ao longo do tempo.

## Como isso pode ajudar a gente?

Sendo direto, um dos requisitos de avaliação da matéria é ter boa parte do código coberto por testes. Porém, acredito que não precisaremos de testes muito elaborados e nem de escrever os testes um por um; o importante vai ser integrar a prática de teste à nossa prática de entrega de código, de forma automatizada.
