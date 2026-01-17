from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from database import Base
from datetime import date, datetime

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    position = Column(String)
    doj = Column(Date, default=date.today)

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    check_in = Column(DateTime, default=datetime.now)
    check_out = Column(DateTime, nullable=True)