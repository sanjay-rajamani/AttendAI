from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database.base import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, nullable=False)

    day = Column(String, nullable=False)

    period = Column(Integer, nullable=False)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    status = Column(String, nullable=False)

    source = Column(String, default="Manual")

    remarks = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    subject = relationship("Subject")