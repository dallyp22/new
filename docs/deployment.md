# Deployment Guide

## Local Development

```bash
docker compose -f infra/docker-compose.yaml up --build
```

## DigitalOcean App Platform

1. Create new App, connect your GitHub repo.
2. Add services for backend, model server, frontend.
3. Set environment variables (`ALPACA_KEY`, `ALPACA_SECRET`, `DB_URL`, etc.).
4. Deploy!
