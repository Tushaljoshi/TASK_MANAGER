# Task Manager Backend API

## 🛠 Tech Stack
- Python Flask
- PostgreSQL
- Redis & Celery
- Docker & Docker Compose
- JWT Authentication

## 🚀 Setup Instructions
```bash
git clone <repo>
cd task_manager
cp .env.example .env
docker-compose up --build
```

## 🔑 Authentication Endpoints
| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| POST   | /auth/signup   | Register a new user     |
| POST   | /auth/login    | Login and get JWT token |

## 📦 Task Endpoints
| Method | Endpoint                     | Description                          |
|--------|------------------------------|--------------------------------------|
| POST   | /api/upload-csv              | Upload CSV to load tasks             |
| GET    | /api/tasks                   | List all tasks (paginated)           |
| GET    | /api/tasks?date=YYYY-MM-DD  | Filter tasks by date (cached)        |
| GET    | /api/task/<id>              | Get specific task details            |
| POST   | /api/task                    | Create a new task (auth required)    |
| PUT    | /api/task/<id>              | Update a task (auth + RBAC)          |
| DELETE | /api/task/<id>              | Soft delete a task (auth + RBAC)     |

## 🧪 Testing
```bash
pytest
```

## ✅ Features
- Secure JWT Authentication
- Role-Based Access Control
- CSV Importing
- Audit Logging
- Caching with Redis
- Task Queue with Celery
- Rate Limiting
- Alembic Migrations

---
Built with ❤️ by your backend.
