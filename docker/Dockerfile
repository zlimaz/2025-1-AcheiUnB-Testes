# Use a imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt /app/

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia o código para dentro do container
COPY . /app/

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
