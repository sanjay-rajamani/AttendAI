from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Timetable(Base):
    __tablename__ = "timetable"

    id = Column(Integer, primary_key=True, index=True)

    day = Column(String, nullable=False)

    period = Column(Integer, nullable=False)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    room = Column(String)

    start_time = Column(String)

    end_time = Column(String)

    subject = relationship("Subject")