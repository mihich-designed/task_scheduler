# Тестовое задание: Мини API для списка задач

## Endpoints

- POST /tasks
- GET /tasks
- GET /tasks/{task_id}

## Локальный запуск
docker compose up --build

## API
http://localhost:9000

## Swagger UI
http://localhost:9000/docs

## Тесты
uv run pytest

## Архитектура
- api.py — API/controller слой
- service.py — бизнес-логика и in-memory storage
- schemas.py — DTO и валидация
- models.py — доменная модель и enum