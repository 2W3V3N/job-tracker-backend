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
.\.venv\Scripts\activate

```
## 2. Install dependencies

```bash
pip install -r requirements.txt
```
## 3. Start the server

```bash
python -m uvicorn app.main:app --reload
```
## 4. Open in browser

Swagger documentation:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health

---

## Why I Built This Project

I built this project to:

Practice backend development

Understand REST API architecture

Learn database integration

Prepare for iOS + backend integration

Build a professional GitHub portfolio

This backend is intended to be connected to a future iOS application.

---
## Next Planned Improvements

Update endpoint (PUT /applications/{id})

Filtering and search

User authentication

Docker support

Cloud deployment

iOS client integration

---

## Author: Magda
Purpose: Internship Portfolio Project
<img width="1667" height="2335" alt="image" src="https://github.com/user-attachments/assets/5e27ceea-5b36-4d2b-8936-fbf8fc1b2f53" />


