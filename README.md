# CoreLink API

A Dockerized Django REST API built with PostgreSQL.

CoreLink is a backend service that provides user authentication and post management functionality using Django REST Framework.  
The project is fully containerized using Docker for consistent development and deployment environments.

---

## 🚀 Features

- Custom User Model
- JWT Authentication (if configured)
- CRUD operations for Posts
- Permission-based access control
- PostgreSQL database integration
- Dockerized environment
- Automatic database migrations on container startup

---

## 🧱 Tech Stack

- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL 16
- Docker & Docker Compose

---

## 📂 Project Structure

```
corelink-api/
│
├── config/               # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/                # Custom user app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
│
├── posts/                # Posts app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory.

You can copy from:

```
.env.example
```

Example configuration:

```
DEBUG=1
POSTGRES_DB=corelink
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## 🐳 Running the Project with Docker

Make sure Docker Desktop is installed and running.

### 1️⃣ Build and Start Containers

```bash
docker compose up --build
```

This will:

- Build the Docker image
- Start PostgreSQL
- Run migrations automatically
- Start Django development server

---

### 2️⃣ Access the API

Open your browser:

```
http://localhost:8000
```

---

## 🧪 API Endpoints (Example)

### Authentication
- `POST /api/users/register/`
- `POST /api/users/login/`
- `GET /api/users/me/`

### Posts
- `GET /api/posts/`
- `POST /api/posts/`
- `PUT /api/posts/<id>/`
- `DELETE /api/posts/<id>/`

---

## 🔄 Running Without Docker (Optional)

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

---

## 🛡 Permissions

Post modification is restricted to the post owner.  
Authenticated access is required for protected endpoints.

---

## 📦 Database

- PostgreSQL runs inside Docker container
- Database data is persisted using Docker volumes

---

## 👨‍💻 Author

Sa'er Hamzeh

---

## 📌 Notes

This project is intended for development purposes.  
For production deployment, use:

- Gunicorn
- Nginx
- Proper environment configuration
- HTTPS