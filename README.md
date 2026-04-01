# FastAPI Auth

A small FastAPI starter project with:

- basic HTTP routes
- async PostgreSQL connectivity via SQLAlchemy
- environment-based configuration using `pydantic-settings`
- auth-related dependencies already installed for future expansion

At the moment, the app exposes simple health, greeting, and database connectivity endpoints.

## Tech Stack

- Python 3.13+
- FastAPI
- SQLAlchemy 2.x
- asyncpg
- Pydantic Settings
- Uvicorn

## Project Structure

```text
.
├── main.py
├── routers/
│   └── auth.py
├── utils/
│   ├── config.py
│   ├── db_helper.py
│   └── schema.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Requirements

- Python `3.13` or newer
- PostgreSQL running locally or remotely
- A valid database URL using an async SQLAlchemy driver such as `postgresql+asyncpg://...`

## Environment Variables

Create a `.env` file in the project root with the following values:

```env
SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
GOOGLE_CLIENT_ID="your_google_client_id"
GOOGLE_CLIENT_SECRET="your_google_client_secret"
SQLALCHEMY_DATABASE_URL="postgresql+asyncpg://username:password@localhost:5432/db_name"
```

Notes:

- `SQLALCHEMY_DATABASE_URL` should use `postgresql+asyncpg://` for the current async DB setup.
- Keep the `.env` file private. It is already ignored by `.gitignore`.

## Installation

### Option 1: Using `uv`

```bash
uv sync
```

### Option 2: Using `pip`

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install sqlalchemy asyncpg uvicorn python-dotenv
```

If you want dependency parity with `pyproject.toml`, prefer `uv sync`.

## Run The App

Start the FastAPI development server:

```bash
uv run uvicorn main:app --reload
```

Or, if you are using a virtual environment directly:

```bash
uvicorn main:app --reload
```

The app will usually be available at:

```text
http://127.0.0.1:8000
```

## Available Endpoints

### `GET /`

Simple health-style endpoint.

Response:

```json
{
  "message": "Hello World!"
}
```

### `GET /hello?name=Aman`

Returns a greeting using the provided query parameter.

Response:

```json
{
  "message": "Hello Aman!"
}
```

### `GET /db-check`

Executes `SELECT 1` against the configured database to confirm connectivity.

Response:

```json
{
  "database": "connected",
  "result": 1
}
```

## API Docs

FastAPI provides interactive docs automatically:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Current Status

This repository is currently a starter base. The `routers/auth.py` module exists, but authentication routes are not implemented yet in the running app.

The project already includes packages for:

- JWT handling
- password hashing
- OAuth/Authlib integration
- database connectivity

## Common Issues

### Missing settings or `.env` values

If startup fails with validation errors for `SECRET_KEY`, `ALGORITHM`, or `SQLALCHEMY_DATABASE_URL`, confirm:

- the `.env` file exists in the project root
- the variable names match exactly
- the database URL is valid

### Database connection errors

If `/db-check` fails:

- make sure PostgreSQL is running
- verify host, port, username, password, and database name
- confirm the URL uses the async driver format: `postgresql+asyncpg://...`

## Next Steps

Natural extensions for this project:

- user registration and login
- JWT access token generation
- password hashing with `passlib`
- Google OAuth login
- SQLAlchemy models and migrations
- route separation with `APIRouter`
