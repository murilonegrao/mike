# Usa a imagem oficial do Python 3.12 na versão slim (mais leve)
FROM python:3.12-slim

# Evita que o Python gere arquivos de bytecode (.pyc)
ENV PYTHONDONTWRITEBYTECODE=1
# Força o Python a printar no console imediatamente (útil para ver logs do docker)
ENV PYTHONUNBUFFERED=1

# Instalar as dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cria usuário não-root (Segurança)
RUN useradd -m -s /bin/bash mike

# Define o diretório de trabalho no container
WORKDIR /app

# Copiamos os requirements primeiro para aproveitar o layer cache do Docker
COPY requirements/ ./requirements/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements/production.txt

# Copia todo o código restante pro container e passa posse ao usuário
COPY --chown=mike:mike . .

# Altera para o usuário seguro antes de rodar comandos do site
USER mike

# O collectstatic precisa simular obrigatoriamente as variáveis sem "default" do nosso production.py, 
# caso contrário, o import da config quebra o `docker build`.
RUN DJANGO_SETTINGS_MODULE="config.settings.production" \
    DJANGO_SECRET_KEY="fake-key-for-build" \
    POSTGRES_DB="dummy" \
    POSTGRES_USER="dummy" \
    POSTGRES_PASSWORD="dummy" \
    POSTGRES_HOST="dummy" \
    python manage.py collectstatic --noinput --clear

# Expor a porta 8000 para trafegar
EXPOSE 8000

# Executa o Gunicorn via processo de usuário isolado
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--threads", "2", "--access-logfile", "-"]
