

## Tech Stack

- Python 3.11.7
- Django 5.0.3
- Django REST Framework
- SQLite (Database)

## Features

- Token-based Authentication
- CRUD operations for tasks
- User-specific task management
- Admin interface for task management

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
cd Task-Tracker-API
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication

- `POST /api-token-auth/`: Get authentication token
  ```bash
  curl -X POST http://localhost:8000/api-token-auth/ \
       -H "Content-Type: application/json" \
       -d '{"username": "your_username", "password": "your_password"}'
  ```

### Tasks

All task endpoints require authentication token in the header: `Authorization: Token your_token`

- **List Tasks**

  ```bash
  GET /api/tasks/
  ```
- **Create Task**

  ```bash
  POST /api/tasks/
  {
    "title": "Task Title",
    "description": "Task Description"
  }
  ```
- **Get Single Task**

  ```bash
  GET /api/tasks/{id}/
  ```
- **Update Task**

  ```bash
  PUT /api/tasks/{id}/
  {
    "title": "Updated Title",
    "description": "Updated Description"
  }
  ```
- **Partial Update Task**

  ```bash
  PATCH /api/tasks/{id}/
  {
    "title": "New Title"
  }
  ```
- **Delete Task**

  ```bash
  DELETE /api/tasks/{id}/
  ```

## Task Model Fields

- `title`: String (required)
- `description`: Text (optional)
- `created_at`: DateTime (auto-set)
- `updated_at`: DateTime (auto-updated)
- `user`: ForeignKey to User (auto-set to current user)

## Testing the API

1. Get authentication token:

```bash
curl -X POST http://localhost:8000/api-token-auth/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

2. Create a new task:

```bash
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token your_token" \
     -d '{"title": "Test Task", "description": "This is a test task"}'
```

3. List all tasks:

```bash
curl -X GET http://localhost:8000/api/tasks/ \
     -H "Authorization: Token your_token"
```

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` using your superuser credentials.

## Project Structure

```
django_task_manager/
├── django_task_manager/    # Main project directory
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── tasks/                  # Tasks app
│   ├── models.py          # Task model definition
│   ├── serializers.py     # API serializers
│   ├── urls.py            # Tasks URL configuration
│   └── views.py           # API views
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## Dependencies

```
django==5.0.3
djangorestframework
django-cors-headers
```
