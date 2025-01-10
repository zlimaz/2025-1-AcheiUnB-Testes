#!/bin/bash
# Saia imediatamente se algum comando falhar
set -e

echo "Entrando no diretório da API..."
cd API/  # Navega para o diretório da API

echo "Iniciando os serviços Docker..."
sudo docker compose up --build  # Constrói e sobe os serviços do Docker