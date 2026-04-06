# MIKE — Training & Fitness Tracker

MIKE is a robust, production-ready Django web application designed to track and organize personal fitness progress, logging training sessions, exercises, and performance metrics securely.

## 🚀 Features

* **Session Management:** Fluidly create, update, and review holistic training sessions.
* **Exercise Library & Sets:** Centralized exercise registry with dynamic, real-time AJAX forms to add Sets, Reps, Weights, and Duration with Zero-UI breaks.
* **Optimized Database Layer:** Solves classic N+1 bottlenecks and protects connection latency via Native SQL Caching and Postgres connection pooling.
* **Container-Native:** Built from the ground-up for scalable, state-of-the-art containerization with Traefik routing, automated static asset delivery (WhiteNoise), and Gunicorn.

## 🛠️ Tech Stack

* **Backend:** Python + Django 6.0
* **Storage & Caching:** PostgreSQL 17 + WhiteNoise Manifest Storage
* **Frontend:** Vanilla JS Modals + Bootstrap 5.3 (Secured via SRI)
* **DevOps / Infrastructure:** Docker, Gunicorn, Custom Docker Compose + Traefik Routing

---

## 💻 Local Development Setup

To run MIKE locally, ensure you have **Python 3.12+** and a running instance of **PostgreSQL**.

### 1. Clone & Environment
```bash
git clone https://github.com/your-username/mike.git
cd mike

# Create and activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Install development requirements (contains debug-toolbar and local DB drivers)
pip install -r requirements/development.txt
```

### 2. Configure Local Secrets

Properly configuring your environment keys is strictly enforced. MIKE relies entirely on its `.env` for setup logic. 

Copy the secure template file:
```bash
cp .env.example .env
```
> **Attention:** Inspect the newly generated `.env` file and insert your local database credentials (`POSTGRES_USER`, `POSTGRES_PASSWORD`) to avoid ImproperlyConfigured exception blocks. For reference on all production flags, permanently refer to `.env.example`.

### 3. Build & Run
```bash
# Prepare the database architecture
python manage.py makemigrations
python manage.py migrate

# (Optional) Create an Admin user to populate global exercises
python manage.py createsuperuser

# Boot the engine!
python manage.py runserver
```
Visit `http://localhost:8000` to dive into the platform.

---

## 🚢 Production Deployment (Docker + Traefik)

MIKE utilizes a hardened, non-root user `Dockerfile` along with a refined `compose.yaml` tailored explicitly for Traefik.

### Pre-Deployment Checks
1. Make sure your production host has `.env` mapped properly with secure strings.
2. Edit `DOMAIN=your_domain.com` in your production vault to accurately route Traefik HTTPS rules.
3. You can safely discard `DJANGO_ALLOWED_HOSTS` inside `.env` in production if your environment handles `DOMAIN` properly on Traefik, though keeping a curated list is safe.

### Spin up the Engine

Upload the repo to your server, guarantee the `.env` sits adjacent to `compose.yaml`, and compose up.
```bash
# Traefik overlay must exist beforehand as an external network
docker compose up --build -d
```
All static files (`staticfiles/`) will automatically be collated, compiled, and properly hashed during image build.

## 🔒 Security Posture

MIKE leverages Subresource Integrity (SRI) over third-party CDNs to defeat Man-In-The-Middle alterations in JavaScript, implements native secure redirect loops via `SECURE_SSL_REDIRECT`, logs errors directly to `stdout` securely for cloud logging agents, and strictly adheres to `DEBUG = False` policies during WSGI handoffs.
