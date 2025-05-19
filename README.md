# Alpaca AI Bot

This project provides a mono-repo for an AI-enhanced trading bot built with FastAPI, React, and containerised services. It targets Alpaca for brokerage and is deployable on DigitalOcean via Docker Compose or Kubernetes.

## Quick Start

```bash
git clone <repo-url>
cd alpaca-ai-bot
cp .env.example .env  # fill in your credentials
docker compose up --build
```

Visit `http://localhost:3000` for the web interface.

## Structure

- **backend/** – FastAPI application and services
- **frontend/** – React application
- **infra/** – Dockerfiles, Compose, and optional k8s manifests
- **docs/** – Additional documentation

## Status

This repository is a work in progress. Many components are stubs or placeholders to be implemented.
