# Configuração do PostgreSQL para Django

### 1. Acessar o PostgreSQL

Para iniciar uma sessão com o PostgreSQL usando o usuário `postgres`:

```bash
sudo -u postgres psql
```

### 2. Criar o Banco de Dados

Dentro do prompt do PostgreSQL, crie um banco de dados para o projeto:

```
sql
```

### 3. Criar o Usuário do Banco de Dados

Crie um usuário com senha segura para gerenciar o banco de dados:

```sql
CREATE USER myprojectuser WITH PASSWORD 'password';
```

### 4. Definir Parâmetros de Conexão

Configure o usuário para otimizar o funcionamento com o Django:

```sql
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

### 5. Conceder Permissões

Dê todas as permissões para o novo usuário administrar o banco de dados:

```sql
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

### 6. Sair do Prompt

Para sair do prompt do PostgreSQL:

```bash
\\q
```

O PostgreSQL agora está configurado para se conectar ao Django.

### 2. Configuração do Django para Utilizar PostgreSQL

Após configurar o banco de dados no PostgreSQL, é necessário configurar o Django para conectar-se a ele. No arquivo `settings.py` do seu projeto Django, adicione as configurações de banco de dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Consultas Otimizadas no ORM do Django para o AcheiUnB

Para otimizar consultas no ORM do Django, no projeto de **Achados e Perdidos na UnB**, algumas práticas ajudam a reduzir o tempo de resposta e a carga no banco de dados.

### 1. **Usar `select_related` para Foreign Keys**

Se as tabelas têm relações `ForeignKey` (ex.: uma tabela `ItensPerdidos` que faz referência a uma tabela `Usuarios`), use `select_related` para trazer dados relacionados em uma única consulta SQL.

```python
itens = ItensPerdidos.objects.select_related('usuario').all()

```

### 2. Utilizar `prefetch_related` para Consultas com ManyToMany

Para relações **muitos-para-muitos** ou **um-para-muitos**, onde não é possível otimizar com `select_related`, utilize `prefetch_related` para carregar as relações em lotes.

```python
# Exemplo: buscando itens perdidos junto com categorias, que é uma relação ManyToMany
itens = Item.objects.prefetch_related('categorias').all()

```

### 3. Limitar os Campos Retornados com `only` e `defer`

Se você não precisa de todos os campos de um modelo, `only` e `defer` permitem especificar os campos que deseja carregar, reduzindo a quantidade de dados transferidos.

```python
# Exemplo: Carregar apenas o nome e descrição dos itens para otimizar o carregamento
itens = Item.objects.only('nome', 'descricao')

```

### 4. Utilizar Filtros para Reduzir a Quantidade de Dados

Aplicar filtros no início da query ajuda a carregar apenas os dados necessários. Combine filtros com `select_related` e `prefetch_related` para otimizar ainda mais.

```python
# Exemplo: Buscar itens perdidos nas últimas 24 horas
from django.utils import timezone
itens = Item.objects.filter(data_perda__gte=timezone.now() - timezone.timedelta(days=1))

```

### 5. Contar Resultados com `count()` em Vez de `len()`

Para evitar a carga desnecessária de objetos ao contar itens, use `count()` em vez de `len()`.

```python
# Exemplo: Contar itens perdidos sem carregar todos os dados
total_itens = Item.objects.filter(encontrado=False).count()

```

### 6. Realizar Anotações com `annotate` para Operações de Agregação

Utilize `annotate` para criar campos agregados nas consultas, como contar itens por categoria.

```python
from django.db.models import Count

# Exemplo: Contar itens perdidos por categoria
categorias = Categoria.objects.annotate(total_itens=Count('item'))

```

### 7. Indexação de Campos no Modelo

Adicionar índices no banco de dados para os campos mais frequentemente filtrados pode melhorar o desempenho. No seu modelo, defina `db_index=True` para esses campos.

```python
# Exemplo: Modelo com indexação de campo
class Item(models.Model):
    nome = models.CharField(max_length=100)
    data_perda = models.DateField(db_index=True)  # campo indexado
    ...

```

### 8. Evitar Consultas N+1

Problemas de N+1 ocorrem quando uma consulta inicial leva a múltiplas consultas adicionais para cada item retornado. `select_related` e `prefetch_related` ajudam a evitar esse problema.

```python
# Solução para problema N+1: Use select_related ou prefetch_related
itens = Item.objects.select_related('local').all()

```

### 9. Consultas Personalizadas com `raw` SQL

Para casos onde o ORM do Django não oferece uma solução ideal em termos de performance, você pode executar consultas SQL diretamente:

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM my_table WHERE ...")
    rows = cursor.fetchall()

```

### 10. Utilização de `F` e `Q` para Consultas Complexas

`F` e `Q` ajudam a realizar operações e combinar condições complexas diretamente no banco de dados:

```python
from django.db.models import F, Q

# Exemplo: Atualizar um campo com base em outro
Item.objects.filter(encontrado=False).update(stock=F('stock') - 1)

# Exemplo: Usar Q para condições OR
Item.objects.filter(Q(categoria='Eletrônicos') | Q(categoria='Documentos'))
```

---

## Ferramentas de Gerenciamento de Banco de Dados com DBeaver

O DBeaver é uma ferramenta de interface gráfica completa e intuitiva para gerenciamento de bancos de dados, compatível com PostgreSQL e outros SGBDs. Com ele, é possível realizar desde operações básicas de administração até análises avançadas de performance, tornando-o ideal para desenvolvedores e administradores de banco de dados.

### 1. Instalação do DBeaver

Baixe e instale a versão mais recente do DBeaver conforme o sistema operacional utilizado. Acesse o site oficial [aqui](https://dbeaver.io/download/) para selecionar a versão apropriada. A instalação é simples e oferece suporte para Windows, macOS e Linux.

### 2. Configuração da Conexão com o PostgreSQL

1. **Abrir o DBeaver**: Após a instalação, abra o DBeaver.
2. **Nova Conexão**: Clique em "New Database Connection" ou use o atalho de conexão na barra de ferramentas.
3. **Selecionar o Banco de Dados**: Escolha "PostgreSQL" na lista de bancos de dados compatíveis e clique em "Next".
4. **Credenciais e Configurações**: Insira as credenciais configuradas no PostgreSQL (nome do banco, usuário, senha, host e porta).
5. **Testar Conexão**: Teste a conexão para garantir que os parâmetros estão corretos e, em seguida, clique em "Finish" para salvar a conexão.

### 3. Execução de Queries e Análise de Dados

Com a conexão estabelecida, você pode gerenciar o banco de dados de forma visual e executar diversas operações:

- **Visualização de Estrutura de Tabelas**: Navegue pela estrutura do banco e visualize tabelas, índices, chaves estrangeiras e constraints.
- **Execução de Queries**: Utilize o editor SQL para escrever e executar consultas SQL. O DBeaver oferece autocompletar e destaque de sintaxe para melhorar a experiência de desenvolvimento.
- **Análise de Índices e Performance**: Inspecione índices e utilize o “Explain Plan” para visualizar o plano de execução de queries, identificando possíveis gargalos e áreas de otimização.
- **Exportação e Importação de Dados**: O DBeaver facilita a importação/exportação de dados para diversos formatos, como CSV, Excel e JSON, útil para backups e integrações.
- **Gerenciamento de Usuários e Permissões**: Configure permissões e gerencie usuários diretamente pelo DBeaver, otimizando a segurança e organização do banco de dados.

![image.png](Configurac%CC%A7a%CC%83o%20do%20PostgreSQL%20para%20Django%2013235f46816580bc8ab7d4ba3dca40f0/image.png)

### Recursos Adicionais do DBeaver

- **Interface Personalizável**: Adapte o DBeaver às suas necessidades com temas e layouts personalizáveis.
- **Suporte a Vários Bancos de Dados**: Gerencie múltiplos tipos de SGBDs em uma única interface, ideal para quem lida com diversos bancos de dados.
- **Histórico de Queries**: Revise e reutilize queries executadas anteriormente por meio do histórico integrado, economizando tempo em consultas recorrentes.

---

### Materiais de Referência

Para mais detalhes sobre cada tópico, consulte:

- [Documentação do Django sobre Integração com PostgreSQL](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes)
- [Tutorial Completo de Configuração Django e PostgreSQL no DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04-pt#criando-o-projeto-django)
- [Guia de Consultas e Otimização no Django ORM](https://docs.djangoproject.com/en/stable/topics/db/optimization/)
- [Documentação do DBeaver](https://dbeaver.io/documentation/)
- Adaptações e contribuições por [Euller Júlio](https://github.com/Potatoyz908).