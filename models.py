from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean
from database import Base
from datetime import date, datetime

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    position = Column(String)
    doj = Column(Date, default=date.today)
    phone = Column(String(20))
    department = Column(String(100))
    status = Column(String(20))
    manager_id = Column(Integer)

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    check_in = Column(DateTime, default=datetime.now)
    check_out = Column(DateTime, nullable=True)
    status = Column(String(20))
    notes = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)