from pydantic import BaseModel


class TemporaryChangeCreate(BaseModel):
    date: str
    period: int
    subject_id: int
    faculty: str | None = None
    reason: str | None = None


class TemporaryChangeResponse(BaseModel):
    id: int
    date: str
    period: int
    subject_id: int
    faculty: str | None = None
    reason: str | None = None

    class Config:
        from_attributes = True