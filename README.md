<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:004a99,100:00ffcc&height=200&section=header&text=SaaS%20Multi-Tenant%20Backend&fontSize=45&fontColor=ffffff&fontAlignY=40&desc=Enterprise%20Multi-Tenant%20Architecture%20with%20FastAPI&descAlignY=65" width="100%"/>

  [![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white&style=for-the-badge)](https://fastapi.tiangolo.com)
  [![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white&style=for-the-badge)](https://docker.com)
  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://python.org)
  [![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
  [![CI](https://github.com/Raphasha27/saas-multitenant-backend/actions/workflows/ci.yml/badge.svg)](https://github.com/Raphasha27/saas-multitenant-backend/actions)
</div>

## Overview

Production-grade multi-tenant SaaS backend built with FastAPI. Features domain-driven architecture, tenant isolation, subscription management, billing integration, and containerized deployment.

## Features

- **Tenant Isolation** — Schema-per-tenant data isolation strategy
- **Subscription Management** — Tiered plan handling with upgrade/downgrade flows
- **Billing Engine** — Invoice generation and payment processing scaffold
- **Auth & RBAC** — JWT-based authentication with role-based access control
- **API Versioning** — Forward-compatible API version strategy
- **Dockerized** — One-command deployment with Docker Compose

## Architecture

```
saas-multitenant-backend/
├── app/
│   ├── auth/            # Authentication & authorization
│   ├── billing/         # Billing & invoice management
│   ├── core/            # Config, middleware, utilities
│   ├── subscriptions/   # Plan & subscription logic
│   ├── tenants/         # Tenant provisioning & isolation
│   └── main.py          # Application entry point
├── Dockerfile           # Container build
├── docker-compose.yml   # Local orchestration
└── requirements.txt     # Dependencies
```

## Quick Start

```bash
git clone https://github.com/Raphasha27/saas-multitenant-backend.git
cd saas-multitenant-backend
cp .env.example .env
docker compose up --build
```

## Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## License

MIT License. See [LICENSE](LICENSE) for details.

---

© 2026 **Kirov Dynamics Technology** | Built by **Koketso Raphasha (Raphasha27)**
