from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Literal

Status = Literal["applied", "interview", "offer", "rejected"]

class ApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=100)
    role: str = Field(min_length=1, max_length=100)
    status: Status = "applied"
    applied_on: date
    link: Optional[str] = None
    notes: Optional[str] = None

class Application(ApplicationCreate):
    id: int
