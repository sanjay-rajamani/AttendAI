from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.base import Base


class TemporaryChange(Base):
    __tablename__ = "temporary_changes"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(String, nullable=False)

    period = Column(Integer, nullable=False)

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    faculty = Column(String)

    reason = Column(String)