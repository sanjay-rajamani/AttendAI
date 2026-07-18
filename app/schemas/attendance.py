from datetime import date
from pydantic import BaseModel


# -----------------------------
# Create Attendance
# -----------------------------
class AttendanceCreate(BaseModel):
    date: date
    day: str
    period: int
    subject_id: int
    status: str
    source: str = "Manual"
    remarks: str | None = None


# -----------------------------
# Update Attendance
# -----------------------------
class AttendanceUpdate(BaseModel):
    status: str
    remarks: str | None = None


# -----------------------------
# Response Model
# -----------------------------
class AttendanceResponse(BaseModel):
    id: int
    date: date
    day: str
    period: int
    subject_id: int
    status: str
    source: str
    remarks: str | None = None

    class Config:
        from_attributes = True