from pydantic import BaseModel


class SubjectCreate(BaseModel):
    subject_code: str
    subject_name: str
    faculty: str


class SubjectUpdate(BaseModel):
    subject_name: str
    faculty: str


class SubjectResponse(BaseModel):
    id: int
    subject_code: str
    subject_name: str
    faculty: str
    total_classes: int
    attended_classes: int

    class Config:
        from_attributes = True