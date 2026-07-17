from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Subject(Base):

    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)

    subject_code = Column(String, unique=True)

    subject_name = Column(String)

    faculty = Column(String)

    total_classes = Column(Integer, default=0)

    attended_classes = Column(Integer, default=0)