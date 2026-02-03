# Job Tracker Backend (FastAPI + SQLite)

Backend REST API for a Job Application Tracker application.  
This project was built as a portfolio project for internship applications.

It demonstrates backend fundamentals such as API design, database usage,
project structure, and testing.

---

## What this project does

- Provides a REST API for managing job applications
- Stores data locally using SQLite
- Supports creating, viewing, and deleting applications
- Includes automatic interactive API documentation
- Includes a basic automated test

---

## Tech Stack

- Python 3
- FastAPI
- Uvicorn
- SQLite
- Pytest
- Git & GitHub

---

## Project Structure

job-tracker-backend/
├── app/
│   ├── main.py        # API routes
│   ├── db.py          # Database setup
│   ├── models.py      # Data models
│   └── __init__.py
├── tests/
│   └── test_health.py
├── requirements.txt
├── README.md
└── .gitignore

---

## API Endpoints

| Method | Endpoint                  | Description                  |
|--------|---------------------------|------------------------------|
| GET    | /health                   | Server status check          |
| POST   | /applications             | Create application           |
| GET    | /applications             | List applications            |
| DELETE | /applications/{id}         | Delete application           |

---

## How to Run Locally (Windows)

### 1. Create virtual environment

Open terminal in project folder and run:

```bash
python -m venv .venv


