# Proyecto Prototipo

Proyecto de ejemplo con backend en Flask, frontend en Vue.js + Vite, base de datos PostgreSQL y monitoreo con Prometheus, Grafana y Alertmanager. También incluye integración continua con GitHub Actions y gestión de base con pgAdmin.

---

## Tecnologías

- Frontend: Vue.js + Vite  
- Backend: Flask (Python)  
- Base de datos: PostgreSQL (Docker)  
- Contenerización: Docker + Docker Compose  
- Monitoreo: Prometheus, Grafana, Alertmanager  
- Gestión BD: pgAdmin 4  
- CI/CD: GitHub Actions (Pytest y Vitest)

---

## Cómo levantar el proyecto

1. Clona el repositorio:

git clone https://github.com/tuusuario/proyecto-prototipo.git
cd proyecto-prototipo

2. Levanta los contenedores:

docker compose up -d --build

3. Accede a los servicios:

Frontend: http://localhost:5173
Backend API: http://localhost:5000/api
PostgreSQL: localhost:5432 (user/password: user/password)
pgAdmin: http://localhost:5050 (admin@admin.com / admin)
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Alertmanager: http://localhost:9093

Base de datos

Al levantar el contenedor de PostgreSQL, se crea la base mydb con una tabla items de ejemplo y datos iniciales.

API endpoints principales
GET /api/items: Lista los items de la base de datos.

GET /api/ping: Endpoint para test de conexión (responde con { "message": "pong" }).

GET /api/metrics: Métricas para Prometheus.

Integración Continua (CI)
El repositorio tiene configurado un workflow de GitHub Actions que corre pruebas en:

Backend con Pytest

Frontend con Vitest (npm test)

Cómo contribuir
Haz un fork y crea una rama nueva para tu feature:
git checkout -b feature/nueva-funcionalidad

Haz commit de tus cambios con mensajes claros.

Abre un pull request.

Contacto
Jorge Arizmendi

