from fastapi import FastAPI, HTTPException
from typing import List
from datetime import date

from .db import get_conn, init_db
from .models import Application, ApplicationCreate

app = FastAPI(title="Job Tracker API", version="1.0.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/applications", response_model=Application, status_code=201)
def create_application(payload: ApplicationCreate):
    with get_conn() as conn:
        cur = conn.execute(
            """
            INSERT INTO applications (company, role, status, applied_on, link, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                payload.company,
                payload.role,
                payload.status,
                payload.applied_on.isoformat(),
                payload.link,
                payload.notes,
            ),
        )
        app_id = cur.lastrowid
        row = conn.execute("SELECT * FROM applications WHERE id = ?", (app_id,)).fetchone()
        conn.commit()

    return Application(
        id=row["id"],
        company=row["company"],
        role=row["role"],
        status=row["status"],
        applied_on=date.fromisoformat(row["applied_on"]),
        link=row["link"],
        notes=row["notes"],
    )

@app.get("/applications", response_model=List[Application])
def list_applications():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM applications ORDER BY id DESC").fetchall()

    return [
        Application(
            id=r["id"],
            company=r["company"],
            role=r["role"],
            status=r["status"],
            applied_on=date.fromisoformat(r["applied_on"]),
            link=r["link"],
            notes=r["notes"],
        )
        for r in rows
    ]

@app.delete("/applications/{app_id}", status_code=204)
def delete_application(app_id: int):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM applications WHERE id = ?", (app_id,))
        conn.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Not found")
