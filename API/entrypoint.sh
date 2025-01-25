#!/bin/bash
# Saia imediatamente se algum comando falhar
set -e

echo "Executando Black para formatar o código..."
black .  # Executa o Black para formatar o código

echo "Executando Ruff para verificar a formatação do código..."
ruff . --fix

if [ "$1" = "python" ] && [ "$2" = "manage.py" ]; then
  echo "Gerando novas migrações..."
  python manage.py makemigrations  # Cria novas migrações com base nos modelos

  echo "Iniciando migrações do banco de dados..."
  python manage.py migrate  # Executa o migrate automaticamente

  echo "Migrações concluídas."
fi

# Executa o comando recebido
exec "$@"
