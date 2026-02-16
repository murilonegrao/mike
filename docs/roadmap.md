Checklist MIKE — Próximos passos (MVP usável + Deploy com Docker)

A) Autenticação (padrão Django)

 Adicionar LoginView e LogoutView no core/urls.py

 Configurar no settings.py:

 LOGIN_URL = "login"

 LOGIN_REDIRECT_URL = "training:training_session_list"

 LOGOUT_REDIRECT_URL = "login"

 Criar templates/accounts/login.html (Bootstrap)

 Adicionar botão “Sair” no layout (logout via POST + csrf)

B) Base template + Bootstrap

 Criar templates/base.html com Bootstrap via CDN

 Navbar com:

 Sessões (training:training_session_list)

 Nova sessão (training:training_session_create)

 Logout (POST)

 Refatorar templates para extends base.html:

 training_session_list.html

 training_session_detail.html

 training_session_form.html

 training_session_confirm_delete.html

 session_exercise_detail.html

 session_exercise_form.html

 session_exercise_confirm_delete.html

 exercise_set_form.html

 exercise_set_confirm_delete.html

C) UX mínima (sem “front bonito”, só usável)

 Padronizar botões (Bootstrap): Salvar / Cancelar / Voltar / Excluir

 Exibir erros de form claramente (alert/invalid-feedback)

 Garantir links “Editar/Excluir” em:

 cada SessionExercise na tela training_session_detail

 cada ExerciseSet na tela session_exercise_detail

 (Opcional) django.contrib.messages para feedback (“salvo”, “excluído”)

D) Settings para produção (compatível com Docker)

 Criar .env (não commitar) com:

 DJANGO_SECRET_KEY

 DJANGO_DEBUG=False

 DJANGO_ALLOWED_HOSTS=seu-dominio.com,localhost

 DATABASE_URL=postgres://... (ou variáveis separadas)

 Ajustar settings.py:

 ler env vars (SECRET_KEY, DEBUG, ALLOWED_HOSTS)

 STATIC_ROOT

 CSRF_TRUSTED_ORIGINS (quando tiver domínio HTTPS)

 SECURE_PROXY_SSL_HEADER (se estiver atrás de reverse proxy)

 cookies secure (quando HTTPS)

E) Docker (deploy padrão)
E1) Dockerfile

 Criar Dockerfile:

 instalar deps

 copiar projeto

 gunicorn como entrypoint/command

E2) docker-compose.yml (mínimo)

 Serviço web (Django + gunicorn)

 Serviço db (PostgreSQL)

 Volume do Postgres

 Volume para staticfiles (opcional)

 Variáveis de ambiente via .env

E3) Entrypoint / comandos

 Rodar automaticamente no container:

 python manage.py migrate

 python manage.py collectstatic --noinput

 Criar superuser (manual, 1x) depois do deploy

E4) Nginx (produção)

Escolha uma:

 Nginx dentro do compose (recomendado)

 ou Nginx fora (se você já tem proxy na VPS)

Checklist Nginx no compose:

 container nginx

 config apontando para web:8000

 servir /static/ (se você montar volume)

 expor porta 80 (e 443 se for terminar TLS ali)

Se você já usa Traefik, dá pra substituir Nginx por Traefik depois. Mas Nginx é o “padrão simples”.

F) Banco: dev x produção

 Confirmar:

 dev pode continuar SQLite

 Docker deploy com Postgres

 Garantir migrations rodando no deploy

G) Deploy na VPS (execução)

 Instalar Docker + docker compose plugin

 Subir stack:

 docker compose up -d --build

 Ver logs:

 docker compose logs -f web

 Criar superuser:

 docker compose exec web python manage.py createsuperuser

 Testar fluxo completo no domínio/IP

H) Documentação “pra GitHub” (mostrar evolução)

 README.md com:

 visão do projeto

 features do MVP

 como rodar local

 como rodar com Docker

 docs/decisions/ (2 ADRs):

 Exercise global + PROTECT

 padrão “R + inline create” no MVP

 docs/notes/ com 2–3 bugs reais que você resolveu (NoReverseMatch, ordering, etc.)