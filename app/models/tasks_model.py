from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass

@dataclass
class Task(db.Model):
    id: int
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    #fk#eisenhower_id = Column(Integer, nullable=False)