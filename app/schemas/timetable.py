from pydantic import BaseModel


# -----------------------------
# Single Timetable Entry
# -----------------------------
class TimetableCreate(BaseModel):
    day: str
    period: int
    subject_id: int
    room: str | None = None


class TimetableUpdate(BaseModel):
    subject_id: int
    room: str | None = None


class TimetableResponse(BaseModel):
    id: int
    day: str
    period: int
    subject_id: int
    room: str | None = None

    class Config:
        from_attributes = True


# -----------------------------
# Weekly Timetable Upload
# -----------------------------
class PeriodEntry(BaseModel):
    period: int
    subject_id: int
    room: str | None = None


class WeeklyTimetable(BaseModel):
    Monday: list[PeriodEntry] = []
    Tuesday: list[PeriodEntry] = []
    Wednesday: list[PeriodEntry] = []
    Thursday: list[PeriodEntry] = []
    Friday: list[PeriodEntry] = []
    Saturday: list[PeriodEntry] = []